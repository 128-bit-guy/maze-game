import pygame.font

from LogicProcessor import *
from MazeRenderer import *


class GameRenderer:
    def __init__(self, logic_processor: LogicProcessor):
        self.logic_processor = logic_processor
        self.maze_renderer = MazeRenderer(self.logic_processor.grid)
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 64)
        self.text_img = None
        self.create_text_img()
        self.logic_processor.player.note_callback = self.create_text_img

    def create_text_img(self):
        self.text_img = self.font.render('Записок собрано: ' + str(self.logic_processor.player.notes) + ' из 16', True,
                                         (255, 255, 255))

    def render(self, screen: pygame.Surface):
        halfw = (screen.get_width() // 2)
        halfh = (screen.get_height() // 2)
        px = self.logic_processor.player.px
        py = self.logic_processor.player.py
        player_radius = self.logic_processor.player.radius
        self.maze_renderer.render(halfw - px, halfh - py, px // 64, py // 64, screen)
        draw.circle(screen, (0, 0, 0), (halfw, halfh), player_radius)
        draw.circle(screen, (255, 255, 255), (halfw, halfh), player_radius - 2)
        for e in self.logic_processor.enemies:
            if self.maze_renderer.grid.get_light(e.px // 64, e.py // 64) > 2:
                dx = e.px - px
                dy = e.py - py
                draw.circle(screen, (255, 255, 255), (halfw + dx, halfh + dy), player_radius)
                draw.circle(screen, (0, 0, 0), (halfw + dx, halfh + dy), player_radius - 2)
        screen.blit(self.text_img, (0, 0))
