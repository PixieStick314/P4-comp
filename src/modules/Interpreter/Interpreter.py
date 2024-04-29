# Interpreter.py
import json
import random
from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor
from modules.Interpreter.Environment import Environment
from modules.Interpreter.Function import Function
from modules.Interpreter.Struct import Struct
from modules.Interpreter.StructInstance import StructInstance


class Interpreter(RogueLangVisitor):
    def __init__(self):
        super().__init__()
        self.verbose = False
        self.environment = Environment(None)

    def set_verbose(self, verbose):
        self.verbose = verbose

    def visitProg(self, ctx:RogueLangParser.ProgContext):
        if self.verbose:
            print("Starting to visit program...")
        for stat in ctx.stat():
            self.visit(stat)
        if self.verbose:
            print("Finished visiting program.")
        return self.visit(ctx.object_())

    def visitObject(self, ctx:RogueLangParser.ObjectContext):
        previous = self.environment
        self.environment = Environment(previous)
        fields = []
        if self.verbose:
            print("Visiting object...")
        for field in ctx.field():
            field_name = self.visit(field)
            fields.append(field_name)
            if self.verbose:
                print(f"Visited field: {field_name}")
        for stat in ctx.stat():
            self.visit(stat)
        self.visit(ctx.procedure())

        output = {}
        for field in fields:
            output[field] = self.environment.get(field)

        self.environment = previous
        if self.verbose:
            print("Object visitation completed.")
        return json.dumps(output)

    def visitField(self, ctx:RogueLangParser.FieldContext):
        field = self.visit(ctx.varDecl())
        if self.verbose:
            print(f"Visiting field: {field}")
        return field

    def visitProcedure(self, ctx:RogueLangParser.ProcedureContext):
        self.visit(ctx.statBlock())

    def visitPrintStat(self, ctx:RogueLangParser.PrintStatContext):
        text = self.visit(ctx.expr())
        print(text)

    def visitVarDeclStat(self, ctx):
        self.visit(ctx.varDecl())

    def visitVarDecl(self, ctx:RogueLangParser.VarDeclContext):
        name = ctx.ID().getText()

        if ctx.assignment():
            value = self.visit(ctx.assignment())
        else:
            value = None

        self.environment.define(name, value)

        if self.verbose:
            print(f"Declared variable '{name}' with value '{value}'")

        return name

    def visitAssignStat(self, ctx:RogueLangParser.AssignStatContext):
        name = ctx.ID().getText()
        value = self.visitAssignment(ctx.assignment())

        if ctx.structFieldAccess():
            fields = []
            for field in ctx.structFieldAccess():
                fields.append(self.visit(field))
            struct = self.environment.get(name)

            value = self.environment.assign_to_struct_field(struct, fields, value)

        if ctx.listAccess():
            index = []
            for i in ctx.listAccess():
                index.append(self.visit(i))
            variable = self.environment.get(name)

            value = self.environment.assign_to_list_element(variable, index, value)

        self.environment.assign(name, value)
        if self.verbose:
            print(f"Assigned variable '{name}' with value '{value}'")

    def visitAssignment(self, ctx:RogueLangParser.AssignmentContext):
        if ctx.struct():
            parent = self.visit(ctx.struct())
            instance = StructInstance(parent)
            return instance
        if self.verbose:
            print(f"Performing assignment for context: {ctx}")
        return self.visitChildren(ctx)

    def visitList(self, ctx:RogueLangParser.ListContext):
        value = []

        for element in ctx.listElement():
            value.append(self.visit(element))

        return value

    def visitListElement(self, ctx:RogueLangParser.ListElementContext):
        return self.visitChildren(ctx)

    def visitPlusEquals(self, ctx:RogueLangParser.PlusEqualsContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        variable = self.environment.get(name)
        if isinstance(variable, list):
            self.environment.plus_equals(name, value)
        elif isinstance(variable, int):
            self.environment.assign(name, (variable + value))

    def visitMinusEquals(self, ctx:RogueLangParser.MinusEqualsContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        variable = self.environment.get(name)
        if isinstance(variable, list):
            self.environment.minus_equals(name, value)
        elif isinstance(variable, int):
            self.environment.assign(name, (variable - value))

    def visitListPop(self, ctx:RogueLangParser.ListPopContext):
        self.environment.get(ctx.ID().getText()).pop()

    def visitStruct(self, ctx:RogueLangParser.StructContext):
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

    def visitStructDef(self, ctx:RogueLangParser.StructDefContext):
        name = ctx.ID().getText()
        fields = []

        for field in ctx.structField():
            fields.append(self.visit(field))
        struct = Struct(name, fields)
        self.environment.define(struct.name, struct)

    def visitStructField(self, ctx:RogueLangParser.StructFieldContext):
        return ctx.ID().getText()

    def visitStatBlock(self, ctx):
        previous = self.environment
        self.environment = Environment(previous)

        if self.verbose:
            print("Visiting statement block...")

        self.visitChildren(ctx)
        self.environment = previous
        if self.verbose:
            print("Completed statement block visitation.")

    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        if self.visit(ctx.expr()) is True:
            self.visit(ctx.statBlock())
        elif ctx.elifStat():
            self.visit(ctx.elifStat())
        elif ctx.elseStat():
            self.visit(ctx.elseStat())

    def visitElifStat(self, ctx:RogueLangParser.ElifStatContext):
        if self.visit(ctx.expr()) is True:
            self.visit(ctx.statBlock())
        elif self.visit(ctx.elifStat()):
            self.visit(ctx.elifStat())

    def visitElseStat(self, ctx:RogueLangParser.ElseStatContext):
        self.visit(ctx.statBlock())

    def visitForLoop(self, ctx):
        previous = self.environment
        self.environment = Environment(previous)

        iterator = ctx.ID(0).getText()
        iterable = self.environment.get(ctx.ID(1).getText())
        self.environment.define(iterator, iterable[0])
        i = 0

        try:
            while i < len(iterable):
                self.environment.values[iterator] = iterable[i]
                self.visit(ctx.statBlock())
                i = i+1
        finally:
            self.environment = previous


    def visitWhileLoop(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.statBlock())

    def visitFunctionDecl(self, ctx:RogueLangParser.FunctionDeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.params()) if ctx.params() is not None else None
        body = ctx.statBlock()

        function = Function(params, body)
        self.environment.define(name, function)
        if self.verbose:
            print(f"Defined function '{name}' with params '{params}'")

    def visitParams(self, ctx:RogueLangParser):
        params = []
        for id in ctx.ID():
            params.append(id.getText())
        return params

    def visitFunctionCall(self, ctx:RogueLangParser.FunctionCallContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.args()) if ctx.args() is not None else None

        previous = self.environment
        self.environment = Environment(previous)
        if args is not None:
            for i in range(len(args)):
                params = self.environment.get(name).params
                self.environment.define(params[i], args[i])

        try:
            self.visit(self.environment.get(name).body)
        except Exception as e:
            return e.args[0]
        finally:
            self.environment = previous

    def visitArgs(self, ctx:RogueLangParser.ArgsContext):
        args = [self.visitChildren(ctx)]
        return args

    def visitReturnStat(self, ctx):
        value = self.visit(ctx.expr())
        raise Exception(value)

    def defaultResult(self):
        # Returns a placeholder for unhandled cases
        return "ERROR"

    def visitListAccess(self, ctx:RogueLangParser.ListAccessContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        else:
            return self.environment.get(ctx.ID().getText())

    def visitListLength(self, ctx:RogueLangParser.ListLengthContext):
        list = self.environment.get(ctx.ID().getText())
        return len(list)

    def visitWhiteNoiseStat(self, ctx:RogueLangParser.WhiteNoiseStatContext):
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

        return array

    def visitRandom(self, ctx:RogueLangParser.RandomContext):
        if ctx.range_():
            bounds = self.visit(ctx.range_())
            return random.randrange(bounds[0], bounds[1])
        elif ctx.ID():
            list = self.environment.get(ctx.ID().getText())
            return random.choice(list)

    def visitRange(self, ctx:RogueLangParser.RangeContext):
        bounds = []
        for i in ctx.expr():
            bounds.append(self.visit(i))
        return bounds

    def visitStructFieldAccess(self, ctx:RogueLangParser.StructFieldAccessContext):
        return ctx.ID().getText()

    def visitExpr(self, ctx):
        if ctx.listAccess():
            name = ctx.ID().getText()
            indices = []
            for index in ctx.listAccess():
                indices.append(self.visit(index))
            return self.environment.get_list_element(name, indices)
        if ctx.structFieldAccess():
            name = ctx.ID().getText()
            field_names = []
            for field_name in ctx.structFieldAccess():
                field_names.append(self.visit(field_name))
            return self.environment.get_struct_field(name, field_names)
        elif ctx.ID():
            return self.environment.get(ctx.ID().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().replace('"', '')
        elif ctx.TRUE() or ctx.getText().lower() == 'true':
            return True
        elif ctx.FALSE() or ctx.getText().lower() == 'false':
            return False
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

        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else None
            operator = ctx.getChild(1).getText()
            if ctx.NOT():
                return not left
            elif right:  # Binary operation
                match operator:
                    case '+':
                        return left + right
                    case '-':
                        return left - right
                    case '*':
                        return left * right
                    case '/':
                        return left / right
                    case '>':
                        return left > right
                    case '<':
                        return left < right
                    case '>=':
                        return left >= right
                    case '<=':
                        return left <= right
                    case '==':
                        return left == right
                    case '!=':
                        return left != right
                    case '%':
                        return left % right
                    case 'and':
                        return left and right
                    case 'or':
                        return left or right
            else:  # Unary operation
                return left
        else:
            return self.defaultResult()
