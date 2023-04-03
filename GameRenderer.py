from MazeRenderer import *


class GameRenderer:
    def __init__(self, logic_processor):
        self.logic_processor = logic_processor
        self.maze_renderer = MazeRenderer(self.logic_processor.grid)

    def render(self, screen):
        halfw = (screen.get_width() // 2)
        halfh = (screen.get_height() // 2)
        px = self.logic_processor.px
        py = self.logic_processor.py
        player_radius = self.logic_processor.player_radius
        self.maze_renderer.render(halfw - px, halfh - py, px // 64, py // 64, screen)
        draw.circle(screen, (0, 0, 0), (halfw, halfh), player_radius)
        draw.circle(screen, (255, 255, 255), (halfw, halfh), player_radius - 2)
