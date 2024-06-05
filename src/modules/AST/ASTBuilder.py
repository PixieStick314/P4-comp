from grammar_files.generated.DungeonParser import DungeonParser
from grammar_files.generated.DungeonVisitor import DungeonVisitor
from modules.AST.Dungeon import Dungeon, MapStat
from modules.AST.expr import *
from modules.AST.stat import *
from modules.Interpreter.Map import Map
from modules.Interpreter.Struct import Struct


class ASTBuilder(DungeonVisitor):

    def visitProg(self, ctx: DungeonParser.ProgContext):
        stats = tuple(self.visit(stat) for stat in ctx.stat())
        map = self.visit(ctx.map_())
        return Dungeon(stats, map)

    def visitMap(self, ctx: DungeonParser.MapContext):
        name = ctx.ID().getText()
        x_dim = int(ctx.INT(0).getText())
        y_dim = int(ctx.INT(1).getText())
        map = Map(name, x_dim, y_dim)

        if ctx.layer():
            layers = [self.visit(layer) for layer in ctx.layer()]
        else:
            layers = None
        if ctx.varDeclStat():
            data = [self.visit(datum) for datum in ctx.varDeclStat()]
        else:
            data = None
        proc = self.visit(ctx.procedure())

        return MapStat(map, layers, data, proc)

    def visitProcedure(self, ctx: DungeonParser.ProcedureContext):
        return self.visit(ctx.statBlock())

    def visitStat(self, ctx: DungeonParser.StatContext):
        return self.visitChildren(ctx)

    def visitLayer(self, ctx: DungeonParser.LayerContext):
        name = ctx.ID().getText()
        if ctx.expr():
            value = self.visit(ctx.expr())
        else:
            value = None
        return LayerExpr(name, value)

    def visitVarDeclStat(self, ctx: DungeonParser.VarDeclStatContext):
        name, value = self.visit(ctx.varDecl())
        return VarDeclStat(name, value)

    def visitVarDecl(self, ctx: DungeonParser.VarDeclContext):
        name = ctx.ID().getText()
        if ctx.assignment():
            value = self.visit(ctx.assignment())
        else:
            value = None
        return name, value

    def visitAssignStat(self, ctx: DungeonParser.AssignStatContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.assignment())
        inner = self.visit(ctx.inner()) if ctx.inner() else None
        return AssignStat(name, value, inner)

    def visitAssignment(self, ctx: DungeonParser.AssignmentContext):
        return self.visitChildren(ctx)

    def visitFunctionDecl(self, ctx: DungeonParser.FunctionDeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.params()) if ctx.params() else None
        body = self.visit(ctx.statBlock())
        return FunctionDeclStat(name, params, body)

    def visitFunctionCall(self, ctx: DungeonParser.FunctionCallContext):
        name = ctx.ID().getText()
        if ctx.args():
            args = self.visit(ctx.args())
        else:
            args = None
        return FunctionCallExpr(name, args)

    def visitListExpr(self, ctx: DungeonParser.ListExprContext):
        if ctx.listElement():
            list = [self.visit(element) for element in ctx.listElement()]
        else:
            list = []
        return ListExpr(list)

    def visitListElement(self, ctx: DungeonParser.ListElementContext):
        return self.visitChildren(ctx)

    def visitListLength(self, ctx: DungeonParser.ListLengthContext):
        list = self.visit(ctx.expr())
        return ListLengthExpr(list)

    def visitListPop(self, ctx: DungeonParser.ListPopContext):
        name = ctx.ID().getText()
        return ListPopStat(name)

    def visitHashTable(self, ctx: DungeonParser.HashTableContext):
        keys = []
        values = []

        for kv_pair in ctx.keyValuePair():
            key, value = self.visit(kv_pair)
            keys.append(key)
            values.append(value)

        return HashTableExpr(keys, values)

    def visitKeyValuePair(self, ctx: DungeonParser.KeyValuePairContext):
        if ctx.ID():
            key = VarExpr(ctx.ID().getText())
        else:
            key = ValueExpr(ctx.STRING().getText().replace('"', ''), "STRING")
        value = self.visit(ctx.expr())
        return key, value

    def visitStruct(self, ctx: DungeonParser.StructContext):
        parent = ctx.ID().getText()
        fields = {}

        for i in range(len(ctx.structField())):
            field_id = self.visit(ctx.structField(i))
            field_value = self.visit(ctx.assignment(i))
            fields[field_id] = field_value

        return StructExpr(parent, fields)

    def visitStructDef(self, ctx: DungeonParser.StructDefContext):
        name = ctx.ID().getText()
        fields = [self.visit(field) for field in ctx.structField()]
        struct = Struct(name, fields)
        return StructDefStat(struct)

    def visitStructField(self, ctx: DungeonParser.StructFieldContext):
        return ctx.ID().getText()

    def visitPlusEquals(self, ctx: DungeonParser.PlusEqualsContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return PlusEqualsStat(name, value)

    def visitMinusEquals(self, ctx: DungeonParser.MinusEqualsContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        return MinusEqualsStat(name, value)

    def visitPrintStat(self, ctx: DungeonParser.PrintStatContext):
        body = tuple(self.visit(expr) for expr in ctx.expr())
        return PrintStat(body)

    def visitIfStat(self, ctx: DungeonParser.IfStatContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.statBlock())
        if ctx.elifStat():
            elifStat = self.visit(ctx.elifStat())
        else:
            elifStat = None
        if ctx.elseStat():
            elseStat = self.visit(ctx.elseStat())
        else:
            elseStat = None
        return IfStat(condition, body, elifStat, elseStat)

    def visitElifStat(self, ctx: DungeonParser.ElifStatContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.statBlock())
        if ctx.elifStat():
            elifStat = self.visit(ctx.elifStat())
        else:
            elifStat = None
        return ElifStat(condition, body, elifStat)

    def visitElseStat(self, ctx: DungeonParser.ElseStatContext):
        body = self.visit(ctx.statBlock())
        return ElseStat(body)

    def visitStatBlock(self, ctx: DungeonParser.StatBlockContext):
        if ctx.stat():
            body = [self.visit(stat) for stat in ctx.stat()]
        else:
            body = None
        return BlockStat(body)

    def visitForLoop(self, ctx: DungeonParser.ForLoopContext):
        iterator = ctx.ID(0).getText()
        if ctx.range_():
            iterable = self.visit(ctx.range_())
        else:
            iterable = ctx.ID(1).getText()
        body = self.visit(ctx.statBlock())
        return ForLoopStat(iterator, iterable, body)

    def visitWhileLoop(self, ctx: DungeonParser.WhileLoopContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.statBlock())
        return WhileLoopStat(condition, body)

    def visitReturnStat(self, ctx: DungeonParser.ReturnStatContext):
        value = self.visit(ctx.expr())
        return ReturnStat(value)

    def visitRandom(self, ctx: DungeonParser.RandomContext):
        if ctx.range_():
            space = self.visit(ctx.range_())
        else:
            space = ctx.ID().getText()
        return RandomExpr(space)

    def visitSeed(self, ctx: DungeonParser.SeedContext):
        seed = self.visit(ctx.expr())
        return SeedStat(seed)

    def visitRange(self, ctx: DungeonParser.RangeContext):
        range = [self.visit(ctx.expr(0)), self.visit(ctx.expr(1))]
        return range

    def visitParams(self, ctx: DungeonParser.ParamsContext):
        return [id.getText() for id in ctx.ID()]

    def visitArgs(self, ctx: DungeonParser.ArgsContext):
        return tuple(self.visit(arg) for arg in ctx.expr())

    def visitInner(self, ctx: DungeonParser.InnerContext):
        if ctx.inner():
            if ctx.DOT():
                inner = self.visit(ctx.inner())
                indices = (self.visit(ctx.structField()),) + inner
            elif ctx.index():
                inner = self.visit(ctx.inner())
                indices = (self.visit(ctx.index()),) + inner
        else:
            if ctx.DOT():
                indices = (self.visit(ctx.structField()),)
            elif ctx.index():
                indices = (self.visit(ctx.index()),)
        return indices

    def visitIndex(self, ctx: DungeonParser.IndexContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.ID():
            return VarExpr(ctx.ID().getText())

    def visitExpr(self, ctx: DungeonParser.ExprContext):
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.random():
            return self.visit(ctx.random())
        elif ctx.inner():
            name = ctx.ID().getText()
            indices = self.visit(ctx.inner())
            return InnerExpr(name, indices)
        elif ctx.listLength():
            return self.visit(ctx.listLength())
        elif ctx.op is not None:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            return BinaryOpExpr(left, op, right)
        elif ctx.POW():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = "^"
            return BinaryOpExpr(left, op, right)
        elif ctx.unary():
            return self.visit(ctx.unary())
        else:
            if ctx.ID():
                return VarExpr(ctx.ID().getText())
            elif ctx.INT():
                value = ctx.INT().getText()
                return ValueExpr(value, "INT")
            elif ctx.FLOAT():
                value = ctx.FLOAT().getText()
                return ValueExpr(value, "FLOAT")
            elif ctx.STRING():
                value = ctx.STRING().getText().replace('"', '')
                return ValueExpr(value, "STRING")
            elif ctx.TRUE():
                return ValueExpr(True, "BOOL")
            elif ctx.FALSE():
                return ValueExpr(False, "BOOL")

    def visitUnary(self, ctx: DungeonParser.UnaryContext):
        value = self.visit(ctx.expr())

        if ctx.NOT():
            op = "NOT"
        elif ctx.SQRT():
            op = "SQRT"
        else:
            op = "GROUP"

        return UnaryOpExpr(value, op)
