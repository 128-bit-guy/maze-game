from MazeGrid import *
from pygame import *
from random import *


class Entity:
    def __init__(self, grid: MazeGrid):
        self.grid = grid
        self.px = None
        self.py = None
        self.radius = 16
        radius = self.radius
        diameter = 2 * self.radius
        self.rect = Rect(-radius, -radius, diameter, diameter)

    def check_collision(self):
        pbx = self.px // 64
        pby = self.py // 64

        for i in range(pbx - 2, pbx + 3):
            for j in range(pby - 2, pby + 3):
                if self.grid.get_block_safe(i, j) in [1, 2]:
                    br = Rect(i * 64 - self.px, j * 64 - self.py, 64, 64)
                    if br.colliderect(self.rect):
                        return True
        return False

    def spawn(self):
        pxa = []
        pya = []
        for i in range(self.grid.get_width()):
            for j in range(self.grid.get_height()):
                if self.grid[i, j] == 0 and self.grid.get_light(i, j) < 3:
                    pxa.append(i)
                    pya.append(j)
        x = randrange(len(pxa))
        self.px = pxa[x] * 64 + 32
        self.py = pya[x] * 64 + 32

    def try_move(self, dx, dy):
        self.px += dx
        self.py += dy
        if self.check_collision():
            self.px -= dx
            self.py -= dy

    def update(self, key_state):
        pass


class Player(Entity):
    def __init__(self, grid):
        super().__init__(grid)
        self.notes = 0
        self.note_callback = None

    def update(self, key_state):
        super().update(key_state)
        if key_state[K_w]:
            self.try_move(0, -1)
        if key_state[K_a]:
            self.try_move(-1, 0)
        if key_state[K_s]:
            self.try_move(0, 1)
        if key_state[K_d]:
            self.try_move(1, 0)
        self.grid.update_light(self.px // 64, self.py // 64)
        if self.grid.get_block_safe(self.px // 64, self.py // 64) == 3:
            self.grid[self.px // 64, self.py // 64] = 0
            self.notes += 1
            self.note_callback()


class Enemy(Entity):
    def __init__(self, grid):
        super().__init__(grid)
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]
        self.wander_generator = None

    def get_wander_direction(self, x, y, pd=10, ld=4):
        if ld == 0:
            return None
        for d in range(4):
            if d != pd:
                nx = x + self.dx[d]
                ny = y + self.dy[d]
                if self.grid.get_block_safe(nx, ny) in [0, 3]:
                    while self.px // 64 != nx or self.py // 64 != ny:
                        yield d
                    og = self.get_wander_direction(nx, ny, d ^ 2, ld - 1)
                    n = next(og, None)
                    while n is not None:
                        yield n
                        n = next(og, None)
                    while self.px // 64 != x or self.py // 64 != y:
                        yield d ^ 2

    def get_player_direction(self):
        cpx = self.px // 64
        cpy = self.py // 64
        cl = self.grid.get_light(cpx, cpy)
        for d in range(4):
            if self.grid.get_light(cpx + self.dx[d], cpy + self.dy[d]) > cl:
                return d
        return None

    def get_direction(self):
        d = self.get_player_direction()
        if d is not None:
            self.wander_generator = None
            return d
        if self.wander_generator is None:
            self.wander_generator = self.get_wander_direction(self.px // 64, self.py // 64)
        d1 = next(self.wander_generator, None)
        if d1 is not None:
            return d1
        self.wander_generator = None
        self.spawn()
        return None

    def update(self, key_state):
        super().update(key_state)
        cd = self.get_direction()
        if cd is not None:
            self.try_move(self.dx[cd], self.dy[cd])
            cdx = self.px - ((self.px // 64) * 64 + 32)
            cdy = self.py - ((self.py // 64) * 64 + 32)
            oc = cdx * self.dx[cd - 1] + cdy * self.dy[cd - 1]
            if oc < -16:
                self.try_move(self.dx[cd - 1], self.dy[cd - 1])
            elif oc > 16:
                self.try_move(-self.dx[cd - 1], -self.dy[cd - 1])

