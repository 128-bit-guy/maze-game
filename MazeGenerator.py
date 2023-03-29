from abc import ABC

from MazeGrid import *
from random import *
from DSU import *


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
        gw = (grid.get_width() + 1) // 2
        gh = (grid.get_height() + 1) // 2
        dsu = DSU(gw * gh)
        av = []
        bv = []
        ex = []
        ey = []
        for i in range(gw):
            for j in range(gh):
                grid[i * 2, j * 2] = 0
                for k in range(2):
                    d = [0, 0]
                    d[k] = 1
                    ni = i + d[0]
                    nj = j + d[1]
                    if 0 <= ni < gw and 0 <= nj < gh:
                        av.append(i + j * gw)
                        bv.append(ni + nj * gh)
                        ex.append(2 * i + d[0])
                        ey.append(2 * j + d[1])
        edg = [i for i in range(len(av))]
        shuffle(edg)
        for e in edg:
            if not dsu.are_united(av[e], bv[e]):
                dsu.unite(av[e], bv[e])
                grid[ex[e], ey[e]] = 0



class DSUMazeGenerator(MazeGenerator):
    def generate(self, grid: MazeGrid):
        pass


generators = [DFSMazeGenerator(), KruskalMazeGenerator(), DSUMazeGenerator()]
