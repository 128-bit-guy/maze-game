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
        init()
        pygame.font.init()
        self.clock = time.Clock()
        self.screen = display.set_mode((300, 300), RESIZABLE)
        display.set_caption("Maze Game", "Maze Game")
        self.running = True
        self.font = pygame.font.SysFont(None, 64)
        self.game_renderer = GameRenderer(self.logic_processor, self.font)

    def run(self):
        while self.running:
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    self.running = False
                    break
                if evt.type == VIDEORESIZE:
                    self.screen = display.set_mode((evt.w, evt.h), RESIZABLE)

            key_state = key.get_pressed()
            self.screen.fill((255, 255, 255))
            if self.logic_processor.won:
                text_img = self.font.render('Победа',
                                            True,
                                            (0, 0, 0))
                halfw = ((self.screen.get_width()- text_img.get_width()) // 2)
                halfh = ((self.screen.get_height() - text_img.get_height()) // 2)
                self.screen.blit(text_img, (halfw, halfh))
            elif self.logic_processor.lost:
                text_img = self.font.render('Поражение',
                                            True,
                                            (0, 0, 0))
                halfw = ((self.screen.get_width()- text_img.get_width()) // 2)
                halfh = ((self.screen.get_height() - text_img.get_height()) // 2)
                self.screen.blit(text_img, (halfw, halfh))
            else:
                self.logic_processor.update(key_state)
                self.game_renderer.render(self.screen)
            display.update()
            self.clock.tick(60)

        pygame.quit()
