from MazeGenerator import *
from pygame import *
from GridPrinter import *


class LogicProcessor:
    def __init__(self, width, height, maze_type):
        self.px = None
        self.py = None

        self.gen = generators[maze_type]
        self.grid = self.gen.generate_grid(width, height)
        self.player_radius = 16
        player_radius = self.player_radius
        player_diameter = 2 * self.player_radius
        self.player_rect = Rect(-player_radius, -player_radius, player_diameter, player_diameter)

        print(print_grid(self.grid))

        self.notes = 0

        self.note_callback = None

        self.spawn_player()

    def spawn_player(self):
        pxa = []
        pya = []
        for i in range(self.grid.get_width()):
            for j in range(self.grid.get_height()):
                if self.grid[i, j] == 0:
                    pxa.append(i)
                    pya.append(j)
        x = randrange(len(pxa))
        self.px = pxa[x] * 64 + 32
        self.py = pya[x] * 64 + 32

    def check_collision(self):
        pbx = self.px // 64
        pby = self.py // 64

        for i in range(pbx - 2, pbx + 3):
            for j in range(pby - 2, pby + 3):
                if self.grid.get_block_safe(i, j) in [1, 2]:
                    br = Rect(i * 64 - self.px, j * 64 - self.py, 64, 64)
                    if br.colliderect(self.player_rect):
                        return True
        return False

    def try_move(self, dx, dy):
        self.px += dx
        self.py += dy
        if self.check_collision():
            self.px -= dx
            self.py -= dy

    def update(self, key_state):
        if key_state[K_w]:
            self.try_move(0, -1)
        if key_state[K_a]:
            self.try_move(-1, 0)
        if key_state[K_s]:
            self.try_move(0, 1)
        if key_state[K_d]:
            self.try_move(1, 0)
        self.grid.update_light(self.px // 64, self.py // 64)
        if self.grid.get_block_safe(self.px // 64, self.py // 64) == 3:
            self.grid[self.px // 64, self.py // 64] = 0
            self.notes += 1
            self.note_callback()
