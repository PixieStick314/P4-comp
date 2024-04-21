import json

from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor
from modules.Interpreter.Environment import Environment
from modules.Interpreter.Function import Function


class Visitor(RogueLangVisitor):
    def __init__(self):
        super().__init__()
        self.environment = Environment(None)
        self.functions = {}

    def visitProg(self, ctx: RogueLangParser.ProgContext):
        for stat in ctx.stat():
            self.visit(stat)
        return self.visit(ctx.object_())

    def visitObject(self, ctx: RogueLangParser.ObjectContext):
        previous = self.environment
        self.environment = Environment(previous)
        fields = []
        for field in ctx.field():
            fields += self.visit(field)
        for stat in ctx.stat():
            self.visit(stat)
        self.visit(ctx.procedure())

        output = {}
        for field in fields:
            output[field] = self.environment.get(field)

        self.environment = previous
        return json.dumps(output)

    def visitField(self, ctx: RogueLangParser.FieldContext):
        field = self.visit(ctx.varDecl())
        return field

    def visitProcedure(self, ctx: RogueLangParser.ProcedureContext):
        self.visit(ctx.statBlock())

    def visitPrintStat(self, ctx: RogueLangParser.PrintStatContext):
        text = self.visit(ctx.expr())
        print(text)

    def visitVarDecl(self, ctx: RogueLangParser.VarDeclContext):
        name = ctx.ID().getText()

        if ctx.list_():
            value = self.visit(ctx.list_())
        elif ctx.expr():
            value = self.visit(ctx.expr())

        try:
            self.environment.assign(name, value)
        except:
            self.environment.define(name, value)

        return name

    def visitList(self, ctx: RogueLangParser.ListContext):
        value = []

        for expr in ctx.expr():
            value.append(self.visit(expr))

        return value

    def visitListPop(self, ctx: RogueLangParser.ListPopContext):
        if ctx.NUMBER():
            name = ctx.ID(0).getText()
            index = int(ctx.NUMBER().getText())
            self.environment.list_pop(name, index)
        else:
            name = ctx.ID(0).getText()
            index = int(self.environment.get(ctx.ID(1).getText()))
            self.environment.list_pop(name, index)

    def visitPlusEquals(self, ctx: RogueLangParser.PlusEqualsContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.environment.plus_equals(name, value)

    def visitStatBlock(self, ctx):
        previous = self.environment
        self.environment = Environment(self.environment)
        self.visitChildren(ctx)
        self.environment = previous

    def visitIfStat(self, ctx: RogueLangParser.IfStatContext):
        if self.visit(ctx.expr()) is True:
            self.visit(ctx.statBlock())
        elif ctx.elifStat():
            self.visit(ctx.elifStat())
        elif ctx.elseStat():
            self.visit(ctx.elseStat())

    def visitElifStat(self, ctx: RogueLangParser.ElifStatContext):
        if self.visit(ctx.expr()) is True:
            self.visit(ctx.statBlock())
        elif self.visit(ctx.elifStat()):
            self.visit(ctx.elifStat())

    def visitElseStat(self, ctx: RogueLangParser.ElseStatContext):
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

    def visitFunctionDecl(self, ctx: RogueLangParser.FunctionDeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.params()) if ctx.params() is not None else None
        body = ctx.statBlock()

        function = Function(params, body)
        self.functions[name] = function

    def visitParams(self, ctx: RogueLangParser):
        params = [self.visitChildren(ctx)]
        return params

    def visitParam(self, ctx: RogueLangParser.ParamContext):
        name = ctx.ID().getText()
        return name

    def visitFunctionCall(self, ctx: RogueLangParser.FunctionCallContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.args()) if ctx.args() is not None else None

        previous = self.environment
        self.environment = Environment(None)
        if args is not None:
            for i in range(len(args)):
                params = self.functions[name].params
                self.environment.define(params[i], args[i])

        try:
            self.visit(self.functions[name].body)
        except Exception as e:
            return e.args[0]
        finally:
            self.environment = previous

    def visitArgs(self, ctx: RogueLangParser.ArgsContext):
        args = [self.visitChildren(ctx)]
        return args

    def visitReturnStat(self, ctx):
        value = self.visit(ctx.expr())
        raise Exception(value)

    def defaultResult(self):
        # Returns a placeholder for unhandled cases
        return "ERROR"

    def visitListElement(self, ctx: RogueLangParser.ListElementContext):
        if ctx.NUMBER():
            name = ctx.ID(0).getText()
            index = int(ctx.NUMBER().getText())
            return self.environment.get_list_element(name, index)
        else:
            name = ctx.ID(0).getText()
            index = int(self.environment.get(ctx.ID(1).getText()))
            return self.environment.get_list_element(name, index)

    def visitExpr(self, ctx):
        if ctx.ID():
            return self.environment.get(ctx.ID().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.TRUE() or ctx.getText().lower() == 'true':
            return True
        elif ctx.FALSE() or ctx.getText().lower() == 'false':
            return False
        elif ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.listElement():
            return self.visit(ctx.listElement())

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
