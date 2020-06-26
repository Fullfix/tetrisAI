from Figure import Figure
import config


class Tetris:
    def __init__(self, score=0):
        self.score = score
        self.game_over = False
        self.figure = Figure()
        self.field = [[0 for j in range(config.WIDTH)] for i in range(config.HEIGHT)]
    
    def collides(self):
        if self.figure.y < 0 or self.figure.y + self.figure.grid_size > config.HEIGHT:
            return False
        if self.figure.x < 0 or self.figure.x + self.figure.grid_size > config.WIDTH:
            return False
        figure_field = self.figure.get_field()
        for i in self.figure.grid_size:
            for j in self.figure.grid_size:
                if figure_field[i][j] and self.field[self.figure.y + i][self.figure.x + j]:
                    return True
        return False
    
    def new_figure(self):
        self.figure = Figure()
    
    def extend_field(self):
        figure_field = self.figure.get_field()
        for i in self.figure.grid_size:
            for j in self.figure.grid_size:
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
        self.figure.rotate()
        if self.collides():
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
        self.fall()