from MazeGenerator import *
from pygame import *
from GridPrinter import *
from Entity import *


class LogicProcessor:
    def __init__(self, width, height, maze_type):

        self.gen = generators[maze_type]
        self.grid = self.gen.generate_grid(width, height)

        print(print_grid(self.grid))

        self.player = Player(self.grid)
        self.player.spawn()
        self.enemies = [Enemy(self.grid) for _ in range(3)]
        for e in self.enemies:
            e.spawn()
        self.won = False
        self.lost = False

    def update(self, key_state):
        self.player.update(key_state)
        if self.player.notes == 16:
            self.won = True
        for e in self.enemies:
            e.update(key_state)
            if e.px // 64 == self.player.px // 64 and e.py // 64 == self.player.py // 64:
                self.lost = True



