from GridPrinter import *
from MazeGenerator import *
from MazeRenderer import *
from random import *
from pygame import *
import pygame


class MazeGame:
    def __init__(self):
        self.px = None
        self.py = None
        print("Enter width and height of maze")
        width, height = map(int, input().split())
        print("Enter maze generator")
        for g in range(len(generators)):
            print("#" + str(g + 1) + ": " + type(generators[g]).__name__)
        i = int(input())
        self.gen = generators[i - 1]
        self.grid = self.gen.generate_grid(width, height)
        self.player_radius = 16
        self.player_rect = Rect(-self.player_radius, -self.player_radius, 2 * self.player_radius, 2 * self.player_radius)

        print(print_grid(self.grid))

        init()
        self.clock = time.Clock()
        self.screen = display.set_mode((300, 300), RESIZABLE)
        self.running = True

        self.maze_renderer = MazeRenderer(self.grid)

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
                if self.grid.get_block_safe(i, j) != 0:
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

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    break
                if event.type == VIDEORESIZE:
                    self.screen = display.set_mode((event.w, event.h), RESIZABLE)

            key_state = key.get_pressed()
            if key_state[K_w]:
                self.try_move(0, -1)
            if key_state[K_a]:
                self.try_move(-1, 0)
            if key_state[K_s]:
                self.try_move(0, 1)
            if key_state[K_d]:
                self.try_move(1, 0)

            self.screen.fill((255, 255, 255))
            halfw = (self.screen.get_width() // 2)
            halfh = (self.screen.get_height() // 2)
            self.grid.update_light(self.px // 64, self.py // 64)
            self.maze_renderer.render(halfw - self.px, halfh - self.py, self.px // 64, self.py // 64, self.screen)
            draw.circle(self.screen, (0, 0, 0), (halfw, halfh), self.player_radius)
            draw.circle(self.screen, (255, 255, 255), (halfw, halfh), self.player_radius - 2)
            display.update()
            self.clock.tick(60)

        pygame.quit()
