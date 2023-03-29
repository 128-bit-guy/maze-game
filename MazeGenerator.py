from abc import ABC

from MazeGrid import *
from random import *


class MazeGenerator:
    def grow_width(self, width):
        return width

    def grow_height(self, height):
        return height

    def generate(self, grid: MazeGrid):
        raise NotImplementedError()

    def generate_grid(self, width, height):
        width = self.grow_width(width)
        height = self.grow_height(height)
        grid = MazeGrid(width, height, 1)
        self.generate(grid)
        return grid


class ThinBasedMazeGenerator(MazeGenerator, ABC):
    def grow_width(self, width):
        if width % 2 == 0:
            return width + 1
        return super().grow_width(width)

    def grow_height(self, height):
        if height % 2 == 0:
            return height + 1
        return super().grow_height(height)


class DFSMazeGenerator(ThinBasedMazeGenerator):
    def __init__(self):
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def dfs(self, g, bg, x, y, ex, ey):
        if 0 <= x < len(bg) and 0 <= y < len(bg[0]) and not bg[x][y]:
            if ex is not None:
                g[ex, ey] = 0
            gx = x * 2
            gy = y * 2
            g[gx, gy] = 0
            bg[x][y] = True
            co = [i for i in range(4)]
            shuffle(co)
            for i in co:
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                self.dfs(g, bg, nx, ny, gx + self.dx[i], gy + self.dy[i])

    def generate(self, grid: MazeGrid):
        g = [[False] * ((grid.get_height() + 1) // 2) for _ in range((grid.get_width() + 1) // 2)]
        self.dfs(grid, g, 0, 0, None, None)


class KruskalMazeGenerator(ThinBasedMazeGenerator):

    def generate(self, grid: MazeGrid):
        pass


class DSUMazeGenerator(MazeGenerator):
    def generate(self, grid: MazeGrid):
        pass


generators = [DFSMazeGenerator(), KruskalMazeGenerator(), DSUMazeGenerator()]
