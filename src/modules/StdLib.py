from algorithms.aStar import astar
from modules.Interpreter.Function import NativeFunction


class StdLib:
    def __init__(self):
        self.astar = NativeFunction(["start", "goal", "grid"], astar)
