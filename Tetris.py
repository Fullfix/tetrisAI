from Figure import Figure
from collections import deque
import config


class Tetris:
    def __init__(self, score=0):
        self.score = score
        self.counter = 0
        self.game_over = False
        self.figure = Figure()
        self.field = [[0 for j in range(config.WIDTH)] for i in range(config.HEIGHT)]
        self.query = deque([Figure(), Figure()])
        while self.figure == self.query[0] == self.query[1]:
            self.query.pop()
            self.query.append(Figure())
    
    def collides(self):
        figure_field = self.figure.get_field()
        for i in range(self.figure.grid_size):
            for j in range(self.figure.grid_size):
                if figure_field[i][j]:
                    if i + self.figure.y not in range(0, config.HEIGHT):
                        return True
                    if j + self.figure.x not in range(0, config.WIDTH):
                        return True
                    if self.field[self.figure.y + i][self.figure.x + j]:
                        return True
        return False
    
    def new_figure(self):
        self.figure = self.query.popleft()
        self.query.append(Figure())
        while self.figure == self.query[0] == self.query[1]:
            self.query.pop()
            self.query.append(Figure())
    
    def extend_field(self):
        figure_field = self.figure.get_field()
        for i in range(self.figure.grid_size):
            for j in range(self.figure.grid_size):
                if figure_field[i][j]:
                    self.field[self.figure.y + i][self.figure.x + j] = figure_field[i][j]
    
    def fall(self):
        self.figure.y += 1
        if self.collides():
            self.figure.y -= 1
            self.freeze()
    
    def move_left(self):
        self.figure.x -= 1
        if self.collides():
            self.figure.x += 1

    def move_right(self):
        self.figure.x += 1
        if self.collides():
            self.figure.x -= 1

    def rotate(self):
        old_rotation = self.figure.rotation
        old_x = self.figure.x
        old_y = self.figure.y
        self.figure.rotate()
        if not self.collides():
            return
        self.figure.x = old_x + 1
        if not self.collides():
            return
        self.figure.x = old_x + 2
        if not self.collides():
            return
        self.figure.x = old_x - 1
        if not self.collides():
            return
        self.figure.x = old_x - 2
        if not self.collides():
            return
        self.figure.x = old_x
        self.figure.y = old_y + 1
        if not self.collides():
            return
        self.figure.y = old_y - 1
        if not self.collides():
            return
        self.figure.y = old_y
        self.figure.rotation = old_rotation
    
    def break_lines(self):
        lines = 0
        for i in range(config.HEIGHT):
            zeros = 0
            for j in range(config.WIDTH):
                if not self.field[i][j]:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(config.WIDTH):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2
    
    def freeze(self):
        self.extend_field()
        self.break_lines()
        self.new_figure()
        if self.collides():
            self.game_over = True
    
    def iteration(self, move):
        self.counter += 1
        if self.game_over:
            return False
        if move == 'L':
            self.move_left()
        if move == 'R':
            self.move_right()
        if move == 'U':
            self.rotate()
        if move == 'D':
            pass
        if self.counter % (config.FPS // 5) == 0:
            self.fall()