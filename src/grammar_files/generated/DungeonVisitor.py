# Generated from C://Users//Muffin//Documents//GitHub//P4-comp//src//grammar_files//Dungeon.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DungeonParser import DungeonParser
else:
    from DungeonParser import DungeonParser

# This class defines a complete generic visitor for a parse tree produced by DungeonParser.

class DungeonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DungeonParser#prog.
    def visitProg(self, ctx:DungeonParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#outputObject.
    def visitOutputObject(self, ctx:DungeonParser.OutputObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#type.
    def visitType(self, ctx:DungeonParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#procedure.
    def visitProcedure(self, ctx:DungeonParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#outputField.
    def visitOutputField(self, ctx:DungeonParser.OutputFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#stat.
    def visitStat(self, ctx:DungeonParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#varDeclStat.
    def visitVarDeclStat(self, ctx:DungeonParser.VarDeclStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#varDecl.
    def visitVarDecl(self, ctx:DungeonParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#assignStat.
    def visitAssignStat(self, ctx:DungeonParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#assignment.
    def visitAssignment(self, ctx:DungeonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#functionDecl.
    def visitFunctionDecl(self, ctx:DungeonParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#functionCall.
    def visitFunctionCall(self, ctx:DungeonParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#list.
    def visitList(self, ctx:DungeonParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#listElement.
    def visitListElement(self, ctx:DungeonParser.ListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#listAccess.
    def visitListAccess(self, ctx:DungeonParser.ListAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#listLength.
    def visitListLength(self, ctx:DungeonParser.ListLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#listPop.
    def visitListPop(self, ctx:DungeonParser.ListPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#struct.
    def visitStruct(self, ctx:DungeonParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#structDef.
    def visitStructDef(self, ctx:DungeonParser.StructDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#structField.
    def visitStructField(self, ctx:DungeonParser.StructFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#structFieldAccess.
    def visitStructFieldAccess(self, ctx:DungeonParser.StructFieldAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#plusEquals.
    def visitPlusEquals(self, ctx:DungeonParser.PlusEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#minusEquals.
    def visitMinusEquals(self, ctx:DungeonParser.MinusEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#printStat.
    def visitPrintStat(self, ctx:DungeonParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#ifStat.
    def visitIfStat(self, ctx:DungeonParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#elifStat.
    def visitElifStat(self, ctx:DungeonParser.ElifStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#elseStat.
    def visitElseStat(self, ctx:DungeonParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#statBlock.
    def visitStatBlock(self, ctx:DungeonParser.StatBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#forLoop.
    def visitForLoop(self, ctx:DungeonParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#whileLoop.
    def visitWhileLoop(self, ctx:DungeonParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#returnStat.
    def visitReturnStat(self, ctx:DungeonParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#whiteNoiseStat.
    def visitWhiteNoiseStat(self, ctx:DungeonParser.WhiteNoiseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#astarStat.
    def visitAstarStat(self, ctx:DungeonParser.AstarStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#bspStat.
    def visitBspStat(self, ctx:DungeonParser.BspStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#perlinNoiseStat.
    def visitPerlinNoiseStat(self, ctx:DungeonParser.PerlinNoiseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#random.
    def visitRandom(self, ctx:DungeonParser.RandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#seed.
    def visitSeed(self, ctx:DungeonParser.SeedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#range.
    def visitRange(self, ctx:DungeonParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#whiteNoiseParams.
    def visitWhiteNoiseParams(self, ctx:DungeonParser.WhiteNoiseParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#astarParams.
    def visitAstarParams(self, ctx:DungeonParser.AstarParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#bspParams.
    def visitBspParams(self, ctx:DungeonParser.BspParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#perlinParams.
    def visitPerlinParams(self, ctx:DungeonParser.PerlinParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#params.
    def visitParams(self, ctx:DungeonParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#args.
    def visitArgs(self, ctx:DungeonParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DungeonParser#expr.
    def visitExpr(self, ctx:DungeonParser.ExprContext):
        return self.visitChildren(ctx)



del DungeonParser