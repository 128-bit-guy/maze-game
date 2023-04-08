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
        self.enemies = [Enemy(self.grid)]
        self.enemies[0].spawn()

    def update(self, key_state):
        self.player.update(key_state)
        for e in self.enemies:
            e.update(key_state)


