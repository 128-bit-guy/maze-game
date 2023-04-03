from GameRenderer import GameRenderer
from MazeRenderer import *
from LogicProcessor import *
import pygame


class MazeGame:
    def __init__(self):
        print("Enter width and height of maze")
        width, height = map(int, input().split())
        print("Enter maze generator")
        for g in range(len(generators)):
            print("#" + str(g + 1) + ": " + type(generators[g]).__name__)
        i = int(input())
        self.logic_processor = LogicProcessor(width, height, i - 1)
        self.game_renderer = GameRenderer(self.logic_processor)
        init()
        self.clock = time.Clock()
        self.screen = display.set_mode((300, 300), RESIZABLE)
        display.set_caption("Maze Game", "Maze Game")
        self.running = True

    def run(self):
        while self.running:
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    self.running = False
                    break
                if evt.type == VIDEORESIZE:
                    self.screen = display.set_mode((evt.w, evt.h), RESIZABLE)

            key_state = key.get_pressed()
            self.logic_processor.update(key_state)
            self.screen.fill((255, 255, 255))
            self.game_renderer.render(self.screen)
            display.update()
            self.clock.tick(60)

        pygame.quit()
