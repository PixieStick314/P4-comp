# Interpreter.py
import json
import random
import math

from modules.AST.expr import StructExpr, Expr
from modules.Interpreter.Environment import Environment
from modules.Interpreter.Function import Function, NativeFunction
from modules.Interpreter.Layer import Layer
from modules.Interpreter.Struct import Struct
from modules.Interpreter.StructInstance import StructInstance
from modules.StdLib import StdLib


class Interpreter:
    def __init__(self):
        self.verbose = False
        self.environment = Environment(None)

        std_lib = StdLib()
        native_functions = vars(std_lib)
        for function in native_functions.keys():
            self.environment.define(function, native_functions[function])

    def visit(self, ctx):
        return ctx.accept(self)

    def set_verbose(self, verbose):
        self.verbose = verbose

    def visitDungeon(self, ctx):
        if self.verbose:
            print("Visiting Dungeon program...")
        try:
            for stat in ctx.stats:
                self.visit(stat)
            result = self.visit(ctx.map)
            if self.verbose:
                print("Finished visiting program.")
            return json.dumps(result)
        except Exception as e:
            print(f"Error visiting program: {str(e)}")
            raise RuntimeError(f"Failed during program execution: {str(e)}")

    def visitMapStat(self, ctx):
        if self.verbose:
            print("Visiting map...")
        previous = self.environment
        self.environment = Environment(previous)
        self.environment.map = ctx.map_def
        try:
            if ctx.data:
                for var in ctx.data:
                    self.visit(var)
                    if self.verbose:
                        print(f"Visited field: {var}")
            elif ctx.layers:
                for layer in ctx.layers:
                    self.visit(layer)
                    if self.verbose:
                        print(f"Visited layer: {layer}")
            else:
                raise RuntimeError("Map has no layers or data.")
            self.visit(ctx.proc)
        except Exception as e:
            print(f"Error during map construction: {str(e)}")
            raise RuntimeError(f"Map creation failed due to: {str(e)}")
        finally:
            layers = {}
            data = {}
            for key in self.environment.values.keys():
                if isinstance(self.environment.values[key], Layer):
                    layers[key] = self.environment.values[key].rows
                else:
                    data[key] = self.environment.values[key]
            map = {self.environment.map.name: {}}
            if layers:
                map[self.environment.map.name]["layers"] = layers
            if data:
                map[self.environment.map.name]["data"] = data
            self.environment = previous
            if self.verbose:
                print("Map visitation completed.")
            return map

    def visitLayerExpr(self, ctx):
        if self.environment.map:
            map = self.environment.map
        else:
            raise RuntimeError(f"Layer creation failed due to no map.")
        if ctx.value:
            layer = Layer(map.dimensions[0], map.dimensions[1], self.visit(ctx.value))
        else:
            layer = Layer(map.dimensions[0], map.dimensions[1], None)
        self.environment.define(ctx.name, layer)

    def visitPrintStat(self, ctx):
        try:
            text = ""
            for expr in ctx.body:
                text += self.visit(expr)
            print(text)
            if self.verbose:
                print(f"Printed: {text}")
        except Exception as e:
            print(f"Error printing text: {str(e)}")
            raise RuntimeError(f"Print statement failed due to: {str(e)}")

    def visitVarDeclStat(self, ctx):
        try:
            if isinstance(ctx.value, StructExpr):
                struct = ctx.value
                for field in struct.fields.keys():
                    struct.fields[field] = self.visit(struct.fields[field])
                value = StructInstance(struct.parent, struct.fields)
            else:
                value = self.visit(ctx.value) if ctx.value else None
            self.environment.define(ctx.name, value)
            if self.verbose:
                print(f"Declared variable '{ctx.name}' with value '{value}'")
        except Exception as e:
            print(f"Error in visitVarDecl for variable '{ctx.name}': {str(e)}")
            raise ValueError(f"Inappropriate value for variable '{ctx.name}': {str(e)}")

    def visitAssignStat(self, ctx):
        name = ctx.name
        value = self.visit(ctx.value)

        if ctx.inner:
            variable = self.environment.get(name)
            if isinstance(self.environment.get(name), Layer):
                variable = variable.rows
            index_list = tuple(self.visit(index) for index in ctx.inner)
            value = self.environment.unpack_and_assign(variable, index_list, value)

        if isinstance(self.environment.get(name), Layer):
            layer = self.environment.get(name)
            if isinstance(value, Layer):
                value = layer
            else:
                raise TypeError(f"Layer {name} cannot be assigned to {value}.")

        self.environment.assign(name, value)
        if self.verbose:
            print(f"Assigned variable '{name}' with value '{value}'")

    def visitListExpr(self, ctx):
        try:
            value = [self.visit(element) for element in ctx.list]
            if self.verbose:
                print(f"Created list with values: {value}")
            return value
        except Exception as e:
            print(f"Error creating list in visitList: {str(e)}")
            raise RuntimeError(f"List creation failed: {str(e)}")

    def visitPlusEqualsStat(self, ctx):
        name = ctx.name
        value = self.visit(ctx.value)
        variable = self.environment.get(name)
        if isinstance(variable, list):
            variable.append(value)
            self.environment.assign(name, variable)
        elif isinstance(variable, int):
            self.environment.assign(name, variable + value)
        else:
            print(f"Error in visitPlusEquals:")
            raise ValueError(f"Invalid operation on variable '{name}'")
        if self.verbose:
            print(f"Performed += on variable '{name}' with increment: {value}")

    def visitMinusEqualsStat(self, ctx):
        name = ctx.name
        value = self.visit(ctx.value)
        variable = self.environment.get(name)
        if isinstance(variable, list):
            variable.remove(value)
            self.environment.assign(name, variable)
        elif isinstance(variable, int):
            self.environment.assign(name, variable - value)
        else:
            print(f"Error in visitMinusEquals:")
            raise ValueError(f"Invalid operation on variable '{name}'")
        if self.verbose:
            print(f"Performed -= on variable '{name}' with decrement: {value}")

    def visitListPopStat(self, ctx):
        try:
            list_var = self.environment.get(ctx.name)
            list_var.pop()
            self.environment.assign(ctx.name, list_var)
            if self.verbose:
                print(f"Popped from list variable '{ctx.name}'.")
            return list_var
        except IndexError:
            print(f"Error: Attempted to pop from an empty list in visitListPop")
            raise RuntimeError("Cannot pop from an empty list")
        except Exception as e:
            print(f"Error in visitListPop: {str(e)}")
            raise RuntimeError(f"List pop operation failed: {str(e)}")

    def visitHashTableExpr(self, ctx):
        hash_table = {}
        for key_value_pair in ctx.keyValuePair():
            key, value = self.visit(key_value_pair)
            hash_table[key] = value

        return hash_table

    def visitStructExpr(self, ctx):
        parent = self.environment.get(ctx.parent)
        if not isinstance(parent, Struct):
            raise RuntimeError(f"Error: {str(parent)} is not a Struct")
        fields = {}
        for field in ctx.value.keys():
            fields[field] = self.visit(ctx.value[field])

        return StructInstance(parent, fields)

    def visitStructDefStat(self, ctx):
        self.environment.define(ctx.struct.name, ctx.struct)

    def visitBlockStat(self, ctx):
        previous = self.environment
        self.environment = Environment(previous)
        if self.verbose:
            print("Visiting statement block...")
        try:
            for stat in ctx.body:
                self.visit(stat)
        except Exception as e:
            if self.verbose:
                print(f"Error in statement block in visitStatBlock: {str(e)}")
            raise  # Re-raise the original exception without modification (It WILL fail if RuntimeError is used)
        finally:
            self.environment = previous
            if self.verbose:
                print("Completed statement block visitation.")

    def visitIfStat(self, ctx):
        try:
            if self.verbose:
                print("Evaluating If statement condition...")
            if self.visit(ctx.condition) is True:
                self.visit(ctx.body)
            elif ctx.elifStat:
                if self.visit(ctx.elifStat):
                    pass
                elif ctx.elseStat:
                    self.visit(ctx.elseStat)
            elif ctx.elseStat:
                self.visit(ctx.elseStat)
        except RuntimeError as e:
            print(f"Error in If statement: {str(e)}")
            raise RuntimeError(f"If statement execution failed: {str(e)}")

    def visitElifStat(self, ctx):
        try:
            if self.verbose:
                print("Evaluating Elif statement condition...")
            if self.visit(ctx.condition) is True:
                self.visit(ctx.body)
                return True
            elif ctx.elifStat:
                return self.visit(ctx.elifStat)
            else:
                return False
        except RuntimeError as e:
            print(f"Error in Elif statement: {str(e)}")
            raise RuntimeError(f"Elif statement execution failed: {str(e)}")

    def visitElseStat(self, ctx):
        try:
            if self.verbose:
                print("Executing Else block...")
            self.visit(ctx.body)
        except RuntimeError as e:
            print(f"Error in Else statement: {str(e)}")
            raise RuntimeError(f"Else statement execution failed: {str(e)}")

    def visitForLoopStat(self, ctx):
        if self.verbose:
            print("Starting For loop...")
        previous = self.environment
        self.environment = Environment(previous)
        iterator = ctx.iterator
        if isinstance(ctx.iterable, list):
            iterable = range(ctx.iterable[0], ctx.iterable[1])
        else:
            iterable = self.environment.get(ctx.iterable)
        self.environment.define(iterator, iterable[0])
        i = 0
        try:
            while i < len(iterable):
                self.environment.values[iterator] = iterable[i]
                self.visit(ctx.body)
                i += 1
        except Exception as e:
            print(f"Error in For loop: {str(e)}")
            raise RuntimeError(f"For loop execution failed: {str(e)}")
        finally:
            self.environment = previous
            if self.verbose:
                print("Completed For loop.")

    def visitWhileLoopStat(self, ctx):
        if self.verbose:
            print("Starting While loop...")
        try:
            while self.visit(ctx.condition):
                self.visit(ctx.body)
        except Exception as e:
            print(f"Error in While loop: {str(e)}")
            raise RuntimeError(f"While loop execution failed: {str(e)}")
        if self.verbose:
            print("Completed While loop.")

    def visitFunctionDeclStat(self, ctx):
        try:
            function = Function(ctx.params, ctx.body)
            self.environment.define(ctx.name, function)
            if self.verbose:
                print(f"Defined function '{ctx.name}' with params '{ctx.params}'")
        except Exception as e:
            error_message = f"Function declaration failed for '{ctx.name}': {str(e)}"
            print(error_message)
            raise RuntimeError(error_message) from e

    def visitFunctionCallExpr(self, ctx):
        if ctx.args:
            args = tuple(self.visit(arg) for arg in ctx.args)
        else:
            args = None
        if self.verbose:
            print(f"Calling function '{ctx.name}' with arguments {args}")
        previous = self.environment
        self.environment = Environment(previous)
        if args is not None:
            for i in range(len(args)):
                params = self.environment.get(ctx.name).params
                self.environment.define(params[i], args[i])

        try:
            function = self.environment.get(ctx.name)
            if isinstance(function, Function):
                self.visit(function.body)
            elif isinstance(function, NativeFunction):
                return function.run(args)
            else:
                raise RuntimeError(f"{ctx.name} is not a function.")
        except ReturnException as e:
            return e.args[0]
        finally:
            self.environment = previous

    def visitReturnStat(self, ctx):
        value = self.visit(ctx.value)
        if self.verbose:
            print(f"Returning value {value}")
        raise ReturnException(value)

    def defaultResult(self):
        # Returns a placeholder for unhandled cases
        return "ERROR: Unhandled Case"

    def visitListLengthExpr(self, ctx):
        try:
            list = self.visit(ctx.list)
            length = len(list)
            if self.verbose:
                print(f"Length of list: {length}")
            return length
        except Exception as e:
            print(f"Error getting length of list:", str(e))
            raise

    def visitSeedStat(self, ctx):
        self.environment.seed = self.visit(ctx.seed)
        random.seed(self.environment.seed)

    def visitRandomExpr(self, ctx):
        try:
            self.environment.check_seed()

            if isinstance(ctx.space, list):
                lower = int(self.visit(ctx.space[0]))
                upper = int(self.visit(ctx.space[1]))
                result = random.randrange(lower, upper)
            else:
                space = self.environment.get(ctx.space)
                result = random.choice(space)

            if self.verbose:
                print(f"Generated random value: {result}")

            return result
        except Exception as e:
            print(f"Error in visitRandom: {str(e)}")
            raise RuntimeError(f"Random value generation failed: {str(e)}")

    def visitInnerExpr(self, ctx):
        if isinstance(ctx.indices[0], Expr):
            indices = (self.visit(ctx.indices[0]),)
        else:
            indices = (ctx.indices[0],)
        if len(ctx.indices) > 1:
            for i in range(1, len(ctx.indices)):
                if isinstance(ctx.indices[i], Expr):
                    indices = indices + (self.visit(ctx.indices[i]),)
                else:
                    indices = indices + (ctx.indices[i],)
        return self.environment.unpack(ctx.name, indices)

    def visitBinaryOpExpr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        match ctx.op:
            case '+': result = left + right
            case '-': result = left - right
            case '*': result = left * right
            case '>': result = left > right
            case '<': result = left < right
            case '>=': result = left >= right
            case '<=': result = left <= right
            case '==': result = left == right
            case '!=': result = left != right
            case '%': result = left % right
            case 'and': result = left and right
            case 'or': result = left or right
            case '/': result = left / right
            case '^': result = pow(left, right)
            case _: raise RuntimeError(f"Operation '{ctx.op}' is not supported")
        return result

    def visitUnaryOpExpr(self, ctx):
        operand = self.visit(ctx.value)
        match ctx.op:
            case 'NOT': result = not operand
            case 'SQRT': result = math.sqrt(operand)
            case 'GROUP': result = operand
            case _: raise RuntimeError(f"Operation '{ctx.op}' is not supported")
        return result

    def visitVarExpr(self, ctx):
        return self.environment.get(ctx.id)

    def visitValueExpr(self, ctx):
        match ctx.type:
            case 'INT': result = int(ctx.value)
            case 'FLOAT': result = float(ctx.value)
            case 'STRING': result = ctx.value
            case 'BOOL': result = ctx.value
            case _: raise RuntimeError(f"Type '{ctx.type}' is not supported")
        return result


class ReturnException(Exception):
    pass
