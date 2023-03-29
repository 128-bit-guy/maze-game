from MazeGrid import *


def print_grid(grid: MazeGrid):
    res = "█" * (grid.get_width() + 2) + "\n"
    for i in range(grid.get_height()):
        res += "█"
        for j in range(grid.get_width()):
            if grid[j, i] == 0:
                res += " "
            else:
                res += "█"
        res += "█\n"
    res += "█" * (grid.get_width() + 2)
    return res
