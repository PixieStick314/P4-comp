class Dungeon:
    def __init__(self, stats, map):
        self.stats = stats
        self.map = map

    def accept(self, visitor):
        return visitor.visitDungeon(self)


class MapStat:
    def __init__(self, map_def, layers, data, proc):
        self.map_def = map_def
        self.layers = layers
        self.data = data
        self.proc = proc

    def accept(self, visitor):
        return visitor.visitMapStat(self)
