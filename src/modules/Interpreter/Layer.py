class Layer:
    def __init__(self, x, y, value):
        self.rows = [[value] * x] * y
