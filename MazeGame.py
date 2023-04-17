from GameRenderer import GameRenderer
from MazeRenderer import *
from LogicProcessor import *
import pygame
from random import *


class MazeGame:
    def __init__(self):
        init()
        pygame.font.init()
        self.clock = time.Clock()
        self.screen = display.set_mode((300, 300), RESIZABLE)
        display.set_caption("Maze Game", "Maze Game")
        self.running = True
        self.font = pygame.font.SysFont(None, 64)
        self.logic_processor = None
        self.game_renderer = None
        self.restart_ticks = 60
        self.text_img = None
        self.init_level()

    def init_level(self):
        width = randrange(20, 30)
        height = randrange(20, 30)
        i = randrange(0, 3)
        self.logic_processor = LogicProcessor(width, height, i - 1)
        self.game_renderer = GameRenderer(self.logic_processor, self.font)

    def update_and_render_pause(self):
        halfw = ((self.screen.get_width()- self.text_img.get_width()) // 2)
        halfh = ((self.screen.get_height() - self.text_img.get_height()) // 2)
        self.screen.blit(self.text_img, (halfw, halfh))
        self.restart_ticks -= 1
        if self.restart_ticks == 0:
            self.restart_ticks = 60
            self.init_level()

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
                self.text_img = self.font.render('Победа',
                                            True,
                                            (0, 0, 0))
                self.update_and_render_pause()
            elif self.logic_processor.lost:
                self.text_img = self.font.render('Поражение',
                                            True,
                                            (0, 0, 0))
                self.update_and_render_pause()
            else:
                self.logic_processor.update(key_state)
                self.game_renderer.render(self.screen)
            display.update()
            self.clock.tick(60)

        pygame.quit()
