# Generated from C:/Users/nedim/Documents/GitHub/P4-comp/src/grammar_files/RogueLang.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by RogueLangParser#dataType.
    def visitDataType(self, ctx:RogueLangParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#baseType.
    def visitBaseType(self, ctx:RogueLangParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#ifStat.
    def visitIfStat(self, ctx:RogueLangParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#ifExpr.
    def visitIfExpr(self, ctx:RogueLangParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#ifBlock.
    def visitIfBlock(self, ctx:RogueLangParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#elifExpr.
    def visitElifExpr(self, ctx:RogueLangParser.ElifExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#elifBlock.
    def visitElifBlock(self, ctx:RogueLangParser.ElifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#elseBlock.
    def visitElseBlock(self, ctx:RogueLangParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#forLoop.
    def visitForLoop(self, ctx:RogueLangParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#whileLoop.
    def visitWhileLoop(self, ctx:RogueLangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#functionDecl.
    def visitFunctionDecl(self, ctx:RogueLangParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#functionCall.
    def visitFunctionCall(self, ctx:RogueLangParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#arrayInit.
    def visitArrayInit(self, ctx:RogueLangParser.ArrayInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#bsp.
    def visitBsp(self, ctx:RogueLangParser.BspContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#params.
    def visitParams(self, ctx:RogueLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#param.
    def visitParam(self, ctx:RogueLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#args.
    def visitArgs(self, ctx:RogueLangParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#randomNumber.
    def visitRandomNumber(self, ctx:RogueLangParser.RandomNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#randomChoice.
    def visitRandomChoice(self, ctx:RogueLangParser.RandomChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#enumDecl.
    def visitEnumDecl(self, ctx:RogueLangParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#enumBody.
    def visitEnumBody(self, ctx:RogueLangParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#enumValue.
    def visitEnumValue(self, ctx:RogueLangParser.EnumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#bspDimension.
    def visitBspDimension(self, ctx:RogueLangParser.BspDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#bspParameters.
    def visitBspParameters(self, ctx:RogueLangParser.BspParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#dimensionList.
    def visitDimensionList(self, ctx:RogueLangParser.DimensionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#minSize.
    def visitMinSize(self, ctx:RogueLangParser.MinSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RogueLangParser#expr.
    def visitExpr(self, ctx:RogueLangParser.ExprContext):
        return self.visitChildren(ctx)



del RogueLangParser