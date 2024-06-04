class Stat:
    def accept(self, visitor):
        pass

class PrintStat(Stat):
    def __init__(self, body):
        self.body = body

    def accept(self, visitor):
        visitor.visitPrintStat(self)

class VarDeclStat(Stat):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visitVarDeclStat(self)

class AssignStat(Stat):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visitAssignStat(self)

class FunctionDeclStat(Stat):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def accept(self, visitor):
        visitor.visitFunctionDeclStat(self)

class IfStat(Stat):
    def __init__(self, condition, body, elifStat, elseStat):
        self.condition = condition
        self.body = body
        self.elifStat = elifStat
        self.elseStat = elseStat

    def accept(self, visitor):
        visitor.visitIfStat(self)

class ElifStat(Stat):
    def __init__(self, condition, body, elifStat):
        self.condition = condition
        self.body = body
        self.elifStat = elifStat

class ElseStat(Stat):
    def __init__(self, body):
        self.body = body

class ForLoopStat(Stat):
    def __init__(self, iterator, iterable, body):
        self.iterator = iterator
        self.iterable = iterable
        self.body = body

    def accept(self, visitor):
        visitor.visitForLoopStat(self)

class WhileLoopStat(Stat):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def accept(self, visitor):
        visitor.visitWhileLoopStat(self)

class BlockStat(Stat):
    def __init__(self, body):
        self.body = body

    def accept(self, visitor):
        visitor.visitBlockStat(self)

class ReturnStat(Stat):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visitReturnStat(self)

class PlusEqualsStat(Stat):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visitPlusEqualsStat(self)

class MinusEqualsStat(Stat):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visitMinusEqualsStat(self)

class ListPopStat(Stat):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visitListPopStat(self)

class StructDefStat(Stat):
    def __init__(self, struct):
        self.struct = struct

    def accept(self, visitor):
        visitor.visitStructDefStat(self)

class SeedStat(Stat):
    def __init__(self, seed):
        self.seed = seed

    def accept(self, visitor):
        visitor.visitSeedStat(self)
