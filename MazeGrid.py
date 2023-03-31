from collections import *

class MazeGrid:
    def __init__(self, width, height, base_block):
        self.grid = [[]] * width
        for i in range(width):
            self.grid[i] = [base_block] * height
        self.light_grid = [[0] * height for _ in range(width)]
        self.lpx = 0
        self.lpy = 0
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def __getitem__(self, item):
        i, j = item
        return self.grid[i][j]

    def __setitem__(self, key, value):
        i, j, = key
        self.grid[i][j] = value

    def get_block_safe(self, i, j):
        if 0 <= i < self.get_width() and 0 <= j < self.get_height():
            return self[i, j]
        else:
            return 2

    def update_light(self, npx, npy):
        x = deque()
        y = deque()
        x.append(self.lpx)
        y.append(self.lpy)
        while len(x) != 0:
            cx = x.pop()
            cy = y.pop()
            if self.get_light(cx, cy) > 2:
                self.light_grid[cx][cy] = 2
                for i in range(4):
                    x.append(cx + self.dx[i])
                    y.append(cy + self.dy[i])

        self.lpx = npx
        self.lpy = npy

        x.append(npx)
        y.append(npy)
        d = deque()
        d.append(7)
        while len(x) > 0:
            cx = x.pop()
            cy = y.pop()
            cd = d.pop()
            if self.get_block_safe(cx, cy) == 0 and cd > 0 and self.get_light(cx, cy) < cd:
                self.light_grid[cx][cy] = cd
                for i in range(4):
                    x.append(cx + self.dx[i])
                    y.append(cy + self.dy[i])
                    d.append(cd - 1)



    def get_light(self, i, j):
        if 0 <= i < self.get_width() and 0 <= j < self.get_height():
            return self.light_grid[i][j]
        else:
            return 0


    def get_width(self):
        return len(self.grid)

    def get_height(self):
        return len(self.grid[0])
