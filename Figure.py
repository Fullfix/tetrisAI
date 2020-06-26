import random
import config


class Figure:
    def __init__(self, x=3, y=0, rotation=0):
        self.x = x
        self.y = y
        shape = random.choice(config.FIGURE_SHAPES)
        self.grid_size = shape['grid_size']
        self.positions = shape['positions']
        self.rotation = rotation
        self.color = shape['color']

    def rotate(self):
        self.rotation += 1
        self.rotation %= 4
    
    def get_field(self):
        Field = [[0 for j in range(self.grid_size)] for i in range(self.grid_size)]
        for block in self.positions[self.rotation]:
            Field[block // self.grid_size][block % self.grid_size] = self.color
        return Field