# binarySpacePartition
import random

def bsp(self, grid, x, y, width, height, depth):
    if depth == 0 or width < 2 or height < 2:
        return grid

    if width > height:
        # Vertical split
        split = random.randint(1, width - 1)
        self.bsp(grid, x, y, split, height, depth - 1)
        self.bsp(grid, x + split, y, width - split, height, depth - 1)
    else:
        # Horizontal split
        split = random.randint(1, height - 1)
        self.bsp(grid, x, y, width, split, depth - 1)
        self.bsp(grid, x, y + split, width, height - split, depth - 1)

    return grid