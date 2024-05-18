from modules.Algorithms.aStar import astar
from modules.Algorithms.WhiteNoise import WhiteNoise
from modules.Interpreter.Function import NativeFunction


class StdLib:
    def __init__(self):
        self.astar = NativeFunction(["start", "goal", "grid"], astar)
        self.WhiteNoise = NativeFunction(["array", "lower", "upper"], WhiteNoise)
