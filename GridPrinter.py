from MazeGrid import *


def print_grid(grid: MazeGrid):
    res = ""
    for i in range(grid.get_height()):
        for j in range(grid.get_width()):
            if grid[j, i] == 0:
                res += " "
            else:
                res += "#"
        res += "\n"
    return res
