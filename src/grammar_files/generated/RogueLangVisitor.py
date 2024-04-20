# Generated from C:/Users/Loke/PycharmProjects/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by RogueLangParser#object.
    def visitObject(self, ctx:RogueLangParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#procedure.
    def visitProcedure(self, ctx:RogueLangParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#field.
    def visitField(self, ctx:RogueLangParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#stat.
    def visitStat(self, ctx:RogueLangParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#varDeclStat.
    def visitVarDeclStat(self, ctx:RogueLangParser.VarDeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#varDecl.
    def visitVarDecl(self, ctx:RogueLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#assignStat.
    def visitAssignStat(self, ctx:RogueLangParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#assignment.
    def visitAssignment(self, ctx:RogueLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:RogueLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#list.
    def visitList(self, ctx:RogueLangParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#listElement.
    def visitListElement(self, ctx:RogueLangParser.ListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#listLength.
    def visitListLength(self, ctx:RogueLangParser.ListLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#listPop.
    def visitListPop(self, ctx:RogueLangParser.ListPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#plusEquals.
    def visitPlusEquals(self, ctx:RogueLangParser.PlusEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#minusEquals.
    def visitMinusEquals(self, ctx:RogueLangParser.MinusEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#printStat.
    def visitPrintStat(self, ctx:RogueLangParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#ifStat.
    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#elifStat.
    def visitElifStat(self, ctx:RogueLangParser.ElifStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#elseStat.
    def visitElseStat(self, ctx:RogueLangParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#statBlock.
    def visitStatBlock(self, ctx:RogueLangParser.StatBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#forLoop.
    def visitForLoop(self, ctx:RogueLangParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#whileLoop.
    def visitWhileLoop(self, ctx:RogueLangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#functionCall.
    def visitFunctionCall(self, ctx:RogueLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#params.
    def visitParams(self, ctx:RogueLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#args.
    def visitArgs(self, ctx:RogueLangParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#returnStat.
    def visitReturnStat(self, ctx:RogueLangParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#random.
    def visitRandom(self, ctx:RogueLangParser.RandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#range.
    def visitRange(self, ctx:RogueLangParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#expr.
    def visitExpr(self, ctx:RogueLangParser.ExprContext):
        return self.visitChildren(ctx)



del RogueLangParser