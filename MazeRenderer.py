from pygame import *
from MazeGrid import *


class MazeRenderer:
    def __init__(self, grid: MazeGrid):
        self.grid = grid
        self.tex = image.load("bricks.jpg")
        self.floor_tex = image.load("floor.jpg")

    def render(self, dx, dy, screen: Surface):
        for i in range(self.grid.get_width()):
            for j in range(self.grid.get_height()):
                if self.grid[i, j] == 1:
                    screen.blit(self.tex, (i * 64 + dx, j * 64 + dy, 64, 64))
                else:
                    screen.blit(self.floor_tex, (i * 64 + dx, j * 64 + dy, 64, 64))
