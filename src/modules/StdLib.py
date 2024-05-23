from modules.Algorithms.aStar import astar
from modules.Algorithms.WhiteNoise import WhiteNoise
from modules.Algorithms.bsp import bsp, departition
from modules.Interpreter.Function import NativeFunction
from modules.Interpreter.Struct import Struct


class StdLib:
    def __init__(self):
        # Standard Library Functions
        self.astar = NativeFunction(["start", "goal", "grid"], astar)
        self.WhiteNoise = NativeFunction(["array", "lower", "upper"], WhiteNoise)
        self.bsp = NativeFunction(["matrix", "depth"], bsp)
        self.departition = NativeFunction(["BSPNode"], departition)

        # Standard Library Structs
        self.BSPNode = Struct("BSPNode", ["split_plane", "depth", "left", "right"])
