from grammar_files.generated.RogueLangParser import RogueLangParser
from grammar_files.generated.RogueLangVisitor import RogueLangVisitor


class Resolver(RogueLangVisitor):
    def __init__(self, interpreter):
        super().__init__()
        self.interpreter = interpreter

    def visitProg(self, ctx:RogueLangParser.ProgContext):
        return self.visitChildren(ctx)


    def visitObject(self, ctx:RogueLangParser.ObjectContext):
        return self.visitChildren(ctx)


    def visitProcedure(self, ctx:RogueLangParser.ProcedureContext):
        return self.visitChildren(ctx)


    def visitField(self, ctx:RogueLangParser.FieldContext):
        return self.visitChildren(ctx)


    def visitStat(self, ctx:RogueLangParser.StatContext):
        return self.visitChildren(ctx)


    def visitVarDecl(self, ctx:RogueLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    def visitFunctionDecl(self, ctx:RogueLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    def visitList(self, ctx:RogueLangParser.ListContext):
        return self.visitChildren(ctx)


    def visitListElement(self, ctx:RogueLangParser.ListElementContext):
        return self.visitChildren(ctx)


    def visitPlusEquals(self, ctx:RogueLangParser.PlusEqualsContext):
        return self.visitChildren(ctx)


    def visitPrintStat(self, ctx:RogueLangParser.PrintStatContext):
        return self.visitChildren(ctx)


    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        return self.visitChildren(ctx)


    def visitElifStat(self, ctx:RogueLangParser.ElifStatContext):
        return self.visitChildren(ctx)


    def visitElseStat(self, ctx:RogueLangParser.ElseStatContext):
        return self.visitChildren(ctx)


    def visitStatBlock(self, ctx:RogueLangParser.StatBlockContext):
        return self.visitChildren(ctx)


    def visitForLoop(self, ctx:RogueLangParser.ForLoopContext):
        return self.visitChildren(ctx)


    def visitWhileLoop(self, ctx:RogueLangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    def visitFunctionCall(self, ctx:RogueLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    def visitReturnStat(self, ctx:RogueLangParser.ReturnStatContext):
        return self.visitChildren(ctx)


    def visitParams(self, ctx:RogueLangParser.ParamsContext):
        return self.visitChildren(ctx)


    def visitParam(self, ctx:RogueLangParser.ParamContext):
        return self.visitChildren(ctx)


    def visitArgs(self, ctx:RogueLangParser.ArgsContext):
        return self.visitChildren(ctx)


    def visitExpr(self, ctx:RogueLangParser.ExprContext):
        return self.visitChildren(ctx)