from GridPrinter import *
from MazeGenerator import *

print("Enter width and height of maze")
width, height = map(int, input().split())
print("Enter maze generator")
for g in range(len(generators)):
    print("#" + str(g + 1) + ": " + type(generators[g]).__name__)
i = int(input())
gen = generators[i - 1]
grid = gen.generate_grid(width, height)

print(print_grid(grid))
