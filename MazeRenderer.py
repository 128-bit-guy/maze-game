from pygame import *
from MazeGrid import *


class MazeRenderer:
    def __init__(self, grid: MazeGrid):
        self.grid = grid
        self.tex = image.load("bricks.jpg")
        self.floor_tex = image.load("floor.jpg")
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def render(self, dx, dy, pbx, pby, screen: Surface):
        xr = screen.get_width() // 128 + 1
        yr = screen.get_height() // 128 + 1
        for i in range(pbx - xr, pbx + xr + 1):
            for j in range(pby - yr, pby + yr + 1):
                if self.grid.get_block_safe(i, j) != 0:
                    screen.blit(self.tex, (i * 64 + dx, j * 64 + dy, 64, 64))
                    light = 0
                    for d in range(4):
                        light = max(light, self.grid.get_light(i + self.dx[d], j + self.dy[d]))

                else:
                    screen.blit(self.floor_tex, (i * 64 + dx, j * 64 + dy, 64, 64))
                    light = self.grid.get_light(i, j)
                brightness = (light * 255) // 7
                screen.fill(Color(brightness, brightness, brightness, 255), (i * 64 + dx, j * 64 + dy, 64, 64), BLEND_MULT)
                    # if i != pbx and j != pby:
                        # screen.fill(Color(205, 205, 205, 50), (i * 64 + dx, j * 64 + dy, 64, 64), BLEND_MULT)
