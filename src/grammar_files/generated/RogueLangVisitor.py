# Generated from C://Users//Muffin//Desktop//4.Semester//Project//Compiler_2//grammar_files//RogueLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RogueLangParser import RogueLangParser
else:
    from RogueLangParser import RogueLangParser

# This class defines a complete generic visitor for a parse tree produced by RogueLangParser.

class RogueLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RogueLangParser#prog.
    def visitProg(self, ctx:RogueLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#stat.
    def visitStat(self, ctx:RogueLangParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#printStat.
    def visitPrintStat(self, ctx:RogueLangParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#varDecl.
    def visitVarDecl(self, ctx:RogueLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#ifStat.
    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#forStat.
    def visitForStat(self, ctx:RogueLangParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#expr.
    def visitExpr(self, ctx:RogueLangParser.ExprContext):
        return self.visitChildren(ctx)



del RogueLangParser