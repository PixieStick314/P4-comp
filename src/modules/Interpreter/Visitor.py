import json

from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor
from modules.Interpreter.Environment import Environment
from modules.Interpreter.Function import Function



class Visitor(RogueLangVisitor):
    def __init__(self):
        super().__init__()
        self.environment = Environment(None)

    def visitProg(self, ctx:RogueLangParser.ProgContext):
        self.visitChildren(ctx)

    def visitObject(self, ctx:RogueLangParser.ObjectContext):
        self.environment = Environment(None)
        fields = []
        for field in ctx.field():
            fields += self.visit(field)
        for stat in ctx.stat():
            self.visit(stat)
        self.visit(ctx.procedure())

        output = {}
        for field in fields:
            output[field] = self.environment.get(field)
        return json.dumps(output)

    def visitField(self, ctx:RogueLangParser.FieldContext):
        field = self.visit(ctx.varDecl())
        return field

    def visitProcedure(self, ctx:RogueLangParser.ProcedureContext):
        self.visit(ctx.statBlock())

    def visitPrintStat(self, ctx:RogueLangParser.PrintStatContext):
        text = self.visit(ctx.expr())
        print(text)

    def visitVarDecl(self, ctx:RogueLangParser.VarDeclContext):
        name = ctx.ID().getText()
        if ctx.expr() is not None:
            value = self.visit(ctx.expr())
        elif ctx.functionCall() is not None:
            value = self.visit(ctx.functionCall())
        else:
            raise RuntimeError("Assignment not valid.")

        try:
            self.environment.assign(name, value)
        except:
            self.environment.define(name, value)

        return name

    def visitStatBlock(self, ctx):
        previous = self.environment
        self.environment = Environment(self.environment)
        self.visitChildren(ctx)
        self.environment = previous

    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        # Initialize output with the 'if' condition and block.
        if self.visit(ctx.expr(0)):
            self.visit(ctx.statBlock(0))
        elif len(ctx.ELIF())>0:
            if self.visit(ctx.expr(1)):
                for i in range(0,len(ctx.ELIF())):
                    self.visit(ctx.statBlock(i+1))
        elif len(ctx.ELSE())>0:
            if self.visit(ctx.expr(len(ctx.expr()))):
                self.visit(ctx.statBlock(len(ctx.statBlock())))

    def visitForLoop(self, ctx):
        name = ctx.varDecl().ID().getText()
        array = self.visit(ctx.expr())
        originalVal = self.environment.get(name)
        for item in array:
            self.environment.assign(name, item)
            for stat in ctx.stat():
                self.visit(stat)
        if originalVal is not None:
            self.variables[name] = originalVal
        else:
            del self.variables[name]

    def visitWhileLoop(self, ctx):
        while self.visit(ctx.expr()):
            self.visit(ctx.stat())

    def visitFunctionDecl(self, ctx:RogueLangParser.FunctionDeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.params()) if ctx.params() is not None else None
        body = ctx.statBlock()

        function = Function(params, body)
        self.environment.define(name, function)

    def visitParams(self, ctx:RogueLangParser):
        params = [self.visitChildren(ctx)]
        return params

    def visitFunctionCall(self, ctx:RogueLangParser.FunctionCallContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.args()) if ctx.args() is not None else None

        previous = self.environment
        self.environment = Environment(None)
        if args is not None:
            for i in range(len(args)):
                self.environment.define(previous.get(name).params[i], args[i])

        func = previous.get(name)
        try:
            self.visit(func.body)
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
        return "''"

    def visitExpr(self, ctx):
        if ctx.ID():
            return ctx.ID().getText()
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
        
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0)) if ctx.expr(0) else ''
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else ''
            op = ctx.getChild(1).getText()
            if op == '[':
                return f'{left}[{right}]'
            else:
                return f'{left} {op} {right}'

        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1)) if ctx.expr(1) else ''
            operator = {'+': '+', '-': '-', '*': '*', '/': '/', '%': '%',
                        '>': '>', '>=': '>=', '<': '<', '<=': '<=',
                        '==': '==', '!=': '!=', 'and': 'and', 'or': 'or', 'not': 'not'}.get(ctx.op.text, ctx.op.text)
            if ctx.NOT():
                return f'not {left}'
            elif right:  # Binary operation
                return f'{left} {operator} {right}'
            else:  # Unary operation
                return left
        else:
            return self.defaultResult()