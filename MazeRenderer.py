from pygame import *
from MazeGrid import *


class MazeRenderer:
    def __init__(self, grid: MazeGrid):
        self.grid = grid
        self.tex = image.load("bricks.jpg")
        self.floor_tex = image.load("floor.jpg")

    def render(self, dx, dy, pbx, pby, screen: Surface):
        xr = screen.get_width() // 128 + 1
        yr = screen.get_height() // 128 + 1
        for i in range(pbx - xr, pbx + xr + 1):
            for j in range(pby - yr, pby + yr + 1):
                if self.grid.get_block_safe(i, j) != 0:
                    screen.blit(self.tex, (i * 64 + dx, j * 64 + dy, 64, 64))
                else:
                    screen.blit(self.floor_tex, (i * 64 + dx, j * 64 + dy, 64, 64))
