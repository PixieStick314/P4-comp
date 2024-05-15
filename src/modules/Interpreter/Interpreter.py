# Interpreter.py
import json
import random
import math
from grammar_files.generated.DungeonParser import DungeonParser
from grammar_files.generated.DungeonVisitor import DungeonVisitor
from modules.Interpreter.Environment import Environment
from modules.Interpreter.Function import Function, NativeFunction
from modules.Interpreter.Struct import Struct
from modules.Interpreter.StructInstance import StructInstance
from modules.StdLib import StdLib


class Interpreter(DungeonVisitor):
    def __init__(self):
        super().__init__()
        self.verbose = False
        self.environment = Environment(None)

        # There's probably a smarter way to do this
        std_lib = StdLib()
        native_functions = vars(std_lib)
        for function in native_functions.keys():
            self.environment.define(function, native_functions[function])


    def set_verbose(self, verbose):
        self.verbose = verbose

    def visitProg(self, ctx:DungeonParser.ProgContext):
        if self.verbose:
            print("Starting to visit program...")
        try:
            for stat in ctx.stat():
                self.visit(stat)
            result = self.visit(ctx.outputObject())
            if self.verbose:
                print("Finished visiting program.")
            return result
        except Exception as e:
            print(f"Error visiting program: {str(e)}")
            raise RuntimeError(f"Failed during program execution: {str(e)}")

    def visitOutputObject(self, ctx:DungeonParser.OutputObjectContext):
        if self.verbose:
            print("Visiting object...")
        previous = self.environment
        self.environment = Environment(previous)
        fields = []
        try:
            for field in ctx.outputField():
                field_name = self.visit(field)
                fields.append(field_name)
                if self.verbose:
                    print(f"Visited field: {field_name}")
            for stat in ctx.stat():
                self.visit(stat)
            self.visit(ctx.procedure())
        except Exception as e:
            print(f"Error during output object construction: {str(e)}")
            raise RuntimeError(f"Output object creation failed due to: {str(e)}")
        finally:
            output = {field: self.environment.get(field) for field in fields}
            self.environment = previous
            if self.verbose:
                print("Object visitation completed.")
            return json.dumps(output)

    def visitOutputField(self, ctx:DungeonParser.OutputFieldContext):
        try:
            field = self.visit(ctx.varDecl())
            if self.verbose:
                print(f"Visiting field: {field}")
            return field
        except Exception as e:
            print(f"Error in field visitation: {str(e)}")
            raise RuntimeError(f"Failed to process field '{field}': {str(e)}")

    def visitProcedure(self, ctx:DungeonParser.ProcedureContext):
        try:
            if self.verbose:
                print("Visiting procedure block...")
            self.visit(ctx.statBlock())
            if self.verbose:
                print("Completed procedure visitation.")
        except Exception as e:
            print(f"Error during procedure execution: {str(e)}")
            raise RuntimeError(f"Procedure execution failed: {str(e)}")

    def visitPrintStat(self, ctx:DungeonParser.PrintStatContext):
        try:
            text = ""
            for expr in ctx.expr():
                text += self.visit(expr)
            print(text)
            if self.verbose:
                print(f"Printed: {text}")
        except Exception as e:
            print(f"Error printing text: {str(e)}")
            raise RuntimeError(f"Print statement failed due to: {str(e)}")

    def visitVarDeclStat(self, ctx):
        try:
            self.visit(ctx.varDecl())
            if self.verbose:
                print("Visited variable declaration statement.")
        except Exception as e:
            print(f"Error declaring variable in visitVarDeclStat: {str(e)}")
            raise RuntimeError(f"Variable declaration failed in statement: {str(e)}")

    def visitVarDecl(self, ctx:DungeonParser.VarDeclContext):
        try:
            name = ctx.ID().getText()
            value = self.visit(ctx.assignment()) if ctx.assignment() else None
            self.environment.define(name, value)
            if self.verbose:
                print(f"Declared variable '{name}' with value '{value}'")
            return name
        except Exception as e:
            print(f"Error in visitVarDecl for variable '{name}': {str(e)}")
            raise ValueError(f"Inappropriate value for variable '{name}': {str(e)}")

    def visitAssignStat(self, ctx:DungeonParser.AssignStatContext):
        name = ctx.ID().getText()
        value = self.visitAssignment(ctx.assignment())

        if ctx.inner():
            variable = self.environment.get(name)
            index_list = self.visit(ctx.inner())
            value = self.environment.unpack_and_assign(variable, index_list, value)

        self.environment.assign(name, value)
        if self.verbose:
            print(f"Assigned variable '{name}' with value '{value}'")

    def visitAssignment(self, ctx:DungeonParser.AssignmentContext):
        if self.verbose:
            print(f"Performing assignment for context: {ctx}")
        try:
            return self.visitChildren(ctx)
        except Exception as e:
            print(f"Error during assignment: {str(e)}")
            raise RuntimeError(f"Assignment processing failed: {str(e)}")

    def visitList(self, ctx:DungeonParser.ListContext):
        try:
            value = [self.visit(element) for element in ctx.listElement()]
            if self.verbose:
                print(f"Created list with values: {value}")
            return value
        except Exception as e:
            print(f"Error creating list in visitList: {str(e)}")
            raise RuntimeError(f"List creation failed: {str(e)}")

    def visitListElement(self, ctx:DungeonParser.ListElementContext):
        try:
            element_value = self.visitChildren(ctx)
            if self.verbose:
                print(f"Visited list element with result: {element_value}")
            return element_value
        except Exception as e:
            print(f"Error processing list element in visitListElement: {str(e)}")
            raise RuntimeError(f"List element processing failed: {str(e)}")

    def visitPlusEquals(self, ctx:DungeonParser.PlusEqualsContext):
        try:
            name = ctx.ID().getText()
            value = self.visit(ctx.expr())
            variable = self.environment.get(name)
            if isinstance(variable, list):
                variable.append(value)
                self.environment.assign(name, variable)
            elif isinstance(variable, int):
                self.environment.assign(name, variable + value)
            if self.verbose:
                print(f"Performed += on variable '{name}' with increment: {value}")
        except Exception as e:
            print(f"Error in visitPlusEquals for '{name}': {str(e)}")
            raise ValueError(f"Invalid operation on variable '{name}': {str(e)}")

    def visitMinusEquals(self, ctx:DungeonParser.MinusEqualsContext):
        try:
            name = ctx.ID().getText()
            value = self.visit(ctx.expr())
            variable = self.environment.get(name)
            if isinstance(variable, list):
                variable.remove(value)
                self.environment.assign(name, variable)
            elif isinstance(variable, int):
                self.environment.assign(name, variable - value)
            if self.verbose:
                print(f"Performed -= on variable '{name}' with decrement: {value}")
        except Exception as e:
            print(f"Error in visitMinusEquals for '{name}': {str(e)}")
            raise ValueError(f"Invalid operation on variable '{name}': {str(e)}")

    def visitListPop(self, ctx:DungeonParser.ListPopContext):
        try:
            list_var = self.environment.get(ctx.ID().getText())
            list_var.pop()
            if self.verbose:
                print(f"Popped from list variable '{ctx.ID().getText()}'.")
        except IndexError:
            print(f"Error: Attempted to pop from an empty list in visitListPop")
            raise ValueError("Cannot pop from an empty list")
        except Exception as e:
            print(f"Error in visitListPop: {str(e)}")
            raise RuntimeError(f"List pop operation failed: {str(e)}")

    def visitHashTable(self, ctx:DungeonParser.HashTableContext):
        hash_table = {}
        for key_value_pair in ctx.keyValuePair():
            key, value = self.visit(key_value_pair)
            hash_table[key] = value

        return hash_table

    def visitKeyValuePair(self, ctx:DungeonParser.KeyValuePairContext):
        if ctx.ID():
            key = self.environment.get(ctx.ID().getText())
        else:
            key = ctx.STRING().getText().replace('"', '')
        value = self.visit(ctx.expr())

        return key, value

    def visitStruct(self, ctx:DungeonParser.StructContext):
        parent = self.environment.get(ctx.ID().getText())
        fields = {}

        for i in range(len(ctx.structField())):
            field_name = self.visit(ctx.structField(i))
            if field_name not in parent.fields:
                raise Exception("Struct {} has no field named {}".format(parent.name, field_name))
            value = self.visit(ctx.assignment(i))
            fields[field_name] = value
        instance = StructInstance(parent, fields)
        return instance

    def visitStructDef(self, ctx:DungeonParser.StructDefContext):
        name = ctx.ID().getText()
        fields = {}

        for field in ctx.structField():
            fields[self.visit(field)] = None
        struct = Struct(name, fields)
        self.environment.define(struct.name, struct)

    def visitStructField(self, ctx:DungeonParser.StructFieldContext):
        return ctx.ID().getText()

    def visitStatBlock(self, ctx):
        previous = self.environment
        self.environment = Environment(previous)
        if self.verbose:
            print("Visiting statement block...")
        try:
            self.visitChildren(ctx)
        except Exception as e:
            if self.verbose:
                print(f"Error in statement block in visitStatBlock: {str(e)}")
            raise  # Re-raise the original exception without modification (It WILL fail if RuntimeError is used)
        finally:
            self.environment = previous
            if self.verbose:
                print("Completed statement block visitation.")

    def visitIfStat(self, ctx:DungeonParser.IfStatContext):
        try:
            if self.verbose:
                print("Evaluating If statement condition...")
            if self.visit(ctx.expr()) is True:
                self.visit(ctx.statBlock())
            elif ctx.elifStat():
                if self.visit(ctx.elifStat()):
                    pass
                elif ctx.elseStat():
                    self.visit(ctx.elseStat())
            elif ctx.elseStat():
                self.visit(ctx.elseStat())
        except Exception as e:
            print(f"Error in If statement: {str(e)}")
            raise RuntimeError(f"If statement execution failed: {str(e)}")

    def visitElifStat(self, ctx:DungeonParser.ElifStatContext):
        try:
            if self.verbose:
                print("Evaluating Elif statement condition...")
            if self.visit(ctx.expr()) is True:
                self.visit(ctx.statBlock())
                return True
            elif ctx.elifStat():
                return self.visit(ctx.elifStat())
            else:
                return False
        except Exception as e:
            print(f"Error in Elif statement: {str(e)}")
            raise RuntimeError(f"Elif statement execution failed: {str(e)}")

    def visitElseStat(self, ctx:DungeonParser.ElseStatContext):
        try:
            if self.verbose:
                print("Executing Else block...")
            self.visit(ctx.statBlock())
        except Exception as e:
            print(f"Error in Else statement: {str(e)}")
            raise RuntimeError(f"Else statement execution failed: {str(e)}")

    def visitForLoop(self, ctx):
        if self.verbose:
            print("Starting For loop...")
        previous = self.environment
        self.environment = Environment(previous)
        iterator = ctx.ID(0).getText()
        if ctx.range_():
            bounds = self.visit(ctx.range_())
            iterable = range(bounds[0], bounds[1])
        else:
            iterable = self.environment.get(ctx.ID(1).getText())
        self.environment.define(iterator, iterable[0])
        i = 0
        try:
            while i < len(iterable):
                self.environment.values[iterator] = iterable[i]
                self.visit(ctx.statBlock())
                i += 1
        except Exception as e:
            print(f"Error in For loop: {str(e)}")
            raise RuntimeError(f"For loop execution failed: {str(e)}")
        finally:
            self.environment = previous
            if self.verbose:
                print("Completed For loop.")

    def visitWhileLoop(self, ctx):
        if self.verbose:
            print("Starting While loop...")
        try:
            while self.visit(ctx.expr()):
                self.visit(ctx.statBlock())
        except Exception as e:
            print(f"Error in While loop: {str(e)}")
            raise RuntimeError(f"While loop execution failed: {str(e)}")
        if self.verbose:
            print("Completed While loop.")

    def visitFunctionDecl(self, ctx:DungeonParser.FunctionDeclContext):
        try:
            name = ctx.ID().getText()
            params = self.visit(ctx.params()) if ctx.params() is not None else None
            body = ctx.statBlock()

            function = Function(params, body)
            self.environment.define(name, function)
            if self.verbose:
                print(f"Defined function '{name}' with params '{params}'")
        except Exception as e:
            error_message = f"Function declaration failed for '{name}': {str(e)}"
            print(error_message)
            raise RuntimeError(error_message) from e

    def visitParams(self, ctx:DungeonParser):
        try:
            params = [id.getText() for id in ctx.ID()]
            if self.verbose:
                print("Visited parameters:", params)
            return params
        except Exception as e:
            print("Error visiting parameters:", str(e))
            raise

    def visitFunctionCall(self, ctx:DungeonParser.FunctionCallContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.args()) if ctx.args() is not None else None
        if self.verbose:
            print(f"Calling function '{name}' with arguments {args}")
        previous = self.environment
        self.environment = Environment(previous)
        if args is not None:
            for i in range(len(args)):
                params = self.environment.get(name).params
                self.environment.define(params[i], args[i])

        try:
            function = self.environment.get(name)
            if isinstance(function, Function):
                self.visit(function.body)
            elif isinstance(function, NativeFunction):
                return function.run(args)
            else:
                raise RuntimeError(f"{name} is not a function.")
        except Exception as e:
            if self.verbose:
                print(f"Error during function call '{name}': {str(e)}")
            return e.args[0]
        finally:
            self.environment = previous

    def visitArgs(self, ctx:DungeonParser.ArgsContext):
        try:
            args = [self.visit(arg) for arg in ctx.expr()]
            if self.verbose:
                print("Visited arguments:", args)
            return args
        except Exception as e:
            print("Error visiting arguments:", str(e))
            raise

    def visitReturnStat(self, ctx):
        try:
            value = self.visit(ctx.expr())
            if self.verbose:
                print(f"Returning value {value}")
            raise Exception(value)
        except Exception as e:
            print("Error during return statement evaluation:", str(e))
            raise

    def defaultResult(self):
        # Returns a placeholder for unhandled cases
        return "ERROR: Unhandled Case"
    def visitListLength(self, ctx:DungeonParser.ListLengthContext):
        try:
            list = self.environment.get(ctx.ID().getText())
            length = len(list)
            if self.verbose:
                print(f"Length of list '{ctx.ID().getText()}': {length}")
            return length
        except Exception as e:
            print(f"Error getting length of list '{ctx.ID().getText()}':", str(e))
            raise

    def visitWhiteNoiseStat(self, ctx:DungeonParser.WhiteNoiseStatContext):
        try:
            array_param = ctx.ID().getText()
            array = self.environment.get(array_param)
            if array is None:
                raise ValueError(f"Array with ID {array_param} not found in environment.") 
            if ctx.range_():
                range_expr = ctx.range_()
                start = int(range_expr.expr(0).getText())
                end = int(range_expr.expr(1).getText())
            else:
                start, end = 0, 1
            for row in array:
                for i in range(len(row)):
                    row[i] = random.randint(start, end)
            if self.verbose:
                print(f"Applied white noise to array {array_param} with range ({start}, {end})")
            return array
        except Exception as e:
            print(f"Error in visitWhiteNoiseStat: {str(e)}")
            raise RuntimeError(f"White noise application failed: {str(e)}")

    def visitSeed(self, ctx:DungeonParser.SeedContext):
        self.environment.seed = self.visit(ctx.expr())
        random.seed(self.environment.seed)

    def visitRandom(self, ctx:DungeonParser.RandomContext):
        try:
            self.environment.check_seed()

            if ctx.range_():
                bounds = self.visit(ctx.range_())
                result = random.randrange(bounds[0], bounds[1])
            elif ctx.ID():
                list = self.environment.get(ctx.ID().getText())
                result = random.choice(list)

            if self.verbose:
                print(f"Generated random value: {result}")

            return result
        except Exception as e:
            print(f"Error in visitRandom: {str(e)}")
            raise RuntimeError(f"Random value generation failed: {str(e)}")

    def visitRange(self, ctx:DungeonParser.RangeContext):
        try:
            bounds = [self.visit(i) for i in ctx.expr()]
            if self.verbose:
                print(f"Evaluated range bounds: {bounds}")
            return bounds
        except Exception as e:
            print(f"Error in visitRange: {str(e)}")
            raise RuntimeError(f"Range evaluation failed: {str(e)}")

    def visitInner(self, ctx:DungeonParser.InnerContext):
        if ctx.inner():
            if ctx.DOT():
                inner = self.visit(ctx.inner())
                index_list = (self.visit(ctx.structField()),) + inner
            elif ctx.index():
                inner = self.visit(ctx.inner())
                index_list = (self.visit(ctx.index()),) + inner
        else:
            if ctx.DOT():
                index_list = (self.visit(ctx.structField()),)
            elif ctx.index():
                index_list = (self.visit(ctx.index()),)
        return index_list

    def visitIndex(self, ctx:DungeonParser.IndexContext):
        if ctx.ID():
            return ["ID", ctx.ID().getText()]
        elif ctx.STRING():
            return ctx.STRING().getText().replace('"', '')
        elif ctx.INT():
            return int(ctx.INT().getText())

    def visitExpr(self, ctx):
        try:
            if ctx.inner():
                name = ctx.ID().getText()
                index_list = self.visit(ctx.inner())
                return self.environment.unpack(name, index_list)
            elif ctx.ID():
                return self.environment.get(ctx.ID().getText())
            elif ctx.STRING():
                return ctx.STRING().getText().replace('"', '')
            elif ctx.TRUE() or ctx.getText().lower() == 'true':
                return True
            elif ctx.FALSE() or ctx.getText().lower() == 'false':
                return False
            elif ctx.NOT():
                expr = self.visit(ctx.expr(0))
                return not expr
            elif ctx.INT():
                return int(ctx.INT().getText())
            elif ctx.FLOAT():
                return float(ctx.FLOAT().getText())
            elif ctx.functionCall():
                return self.visit(ctx.functionCall())
            elif ctx.listLength():
                return self.visit(ctx.listLength())
            elif ctx.random():
                return self.visit(ctx.random())
            elif ctx.SQRT():
                try:
                    return math.sqrt(self.visit(ctx.expr(0)))
                except:
                    raise Exception("Cannot find square root of: " + self.visit(ctx.expr(0)))
            elif ctx.POW():
                try:
                    return pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
                except:
                    raise Exception(
                        "Cannot find power of: " + self.visit(ctx.expr(0)) + " and " + self.visit(ctx.expr(1)))

            elif ctx.getChildCount() == 3:
                left = self.visit(ctx.expr(0))
                if ctx.OPEN_PARENTH():
                    return left
                right = self.visit(ctx.expr(1))
                operator = ctx.op.text
                if (isinstance(left, str) and isinstance(right, str)):
                    return str(left + right)
                elif right is not None:  # Binary operation
                    match operator:
                        case '+': result = left + right
                        case '-': result = left - right
                        case '*': result = left * right
                        case '>': result = left > right
                        case '<': result = left < right
                        case '>=': result = left >= right
                        case '<=': result = left <= right
                        case '==': result = left == right
                        case '!=': result = left != right
                        case'%': result = left % right
                        case'and': result = left and right
                        case'or': result = left or right
                        case '/': result = left / right
                else:  # Unary operation
                    result = left
            else:
                result = self.defaultResult()
            if self.verbose:
                print(f"Evaluated expression result: {result}")
            return result
        except Exception as e:
            print(f"Error in visitExpr: {str(e)}")
            raise RuntimeError(f"Expression evaluation failed: {str(e)}")
