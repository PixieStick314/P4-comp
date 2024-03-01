from RogueLangParser import RogueLangParser
from RogueLangVisitor import RogueLangVisitor

class RogueExecutor(RogueLangVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # For storing variables

    # Override methods from RogueLangVisitor as needed
    def visitPrintStat(self, ctx):
        # Handling a print statement
        text = self.visit(ctx.expr())
        print(text)

    def visitVarDecl(self, ctx):
        # Handling variable declaration
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())  # Evaluate the expression on the right-hand side
        self.variables[name] = value

    def visitExpr(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        # Evaluating an expression

        if ctx.INT():
            return int(ctx.INT().getText())