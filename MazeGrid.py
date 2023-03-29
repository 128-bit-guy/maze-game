class MazeGrid:
    def __init__(self, width, height, base_block):
        self.grid = [[]] * width
        for i in range(width):
            self.grid[i] = [base_block] * height

    def __getitem__(self, item):
        i, j = item
        return self.grid[i][j]

    def __setitem__(self, key, value):
        i, j, = key
        self.grid[i][j] = value

    def get_width(self):
        return len(self.grid)

    def get_height(self):
        return len(self.grid[0])