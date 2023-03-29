from GridPrinter import *
from MazeGenerator import *
from MazeRenderer import *
from pygame import *
import pygame


print("Enter width and height of maze")
width, height = map(int, input().split())
print("Enter maze generator")
for g in range(len(generators)):
    print("#" + str(g + 1) + ": " + type(generators[g]).__name__)
i = int(input())
gen = generators[i - 1]
grid = gen.generate_grid(width, height)

print(print_grid(grid))

init()
clock = time.Clock()
screen = display.set_mode((300, 300), RESIZABLE)
running = True

maze_renderer = MazeRenderer(grid)

px = 32
py = 32

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break
        if event.type == VIDEORESIZE:
            screen = display.set_mode((event.w, event.h), RESIZABLE)

    keyState = key.get_pressed()
    if keyState[K_w]:
        py -= 1
    if keyState[K_a]:
        px -= 1
    if keyState[K_s]:
        py += 1
    if keyState[K_d]:
        px += 1

    screen.fill((255, 255, 255))
    maze_renderer.render((screen.get_width() / 2) - px, (screen.get_height() / 2) - py, screen)
    display.update()
    clock.tick(60)

pygame.quit()
