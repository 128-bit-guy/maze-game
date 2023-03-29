from MazeGrid import *
from GridPrinter import *

grid = MazeGrid(10, 10, 0)

for i in range(grid.get_width()):
    grid[i, i] = 1

print(print_grid(grid))


