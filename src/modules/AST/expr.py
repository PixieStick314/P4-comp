class Expr:
    def accept(self, visitor):
        pass

class FunctionCallExpr(Expr):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def accept(self, visitor):
        return visitor.visitFunctionCallExpr(self)

class RandomExpr(Expr):
    def __init__(self, space):
        self.space = space

    def accept(self, visitor):
        return visitor.visitRandomExpr(self)

class InnerExpr(Expr):
    def __init__(self, name, indices):
        self.name = name
        self.indices = indices

    def accept(self, visitor):
        return visitor.visitInnerExpr(self)

class ListLengthExpr(Expr):
    def __init__(self, list):
        self.list = list

    def accept(self, visitor):
        return visitor.visitListLengthExpr(self)

class BinaryOpExpr(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinaryOpExpr(self)

class UnaryOpExpr(Expr):
    def __init__(self, value, op):
        self.value = value
        self.op = op

    def accept(self, visitor):
        return visitor.visitUnaryOpExpr(self)

class VarExpr(Expr):
    def __init__(self, id):
        self.id = id

    def accept(self, visitor):
        return visitor.visitIDExpr(self)

class ValueExpr(Expr):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visitValueExpr(self)

class StructExpr(Expr):
    def __init__(self, parent, fields):
        self.parent = parent
        self.fields = fields

    def accept(self, visitor):
        return visitor.visitStructExpr(self)

class LayerExpr(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value
