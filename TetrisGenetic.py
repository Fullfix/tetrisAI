from Tetris import Tetris
from Agent import Agent
import numpy as np
import config


class TetrisGenetic(Tetris):
    def __init__(self, agent=None):
        super().__init__()
        self.agent = agent if agent else Agent()
    
    def play(self):
        state = self.get_state()
        move = self.agent.act(state)
        self.iteration(move)
        self.agent.score = self.score
        self.agent.totaltime = self.counter
    
    def reset(self):
        self.agent.score = 0
        self.agent.totaltime = 0
        self.__init__(self.agent)
    
    def get_state(self):
        X = np.zeros((config.HEIGHT, config.WIDTH))
        for i in range(config.HEIGHT):
            for j in range(config.WIDTH):
                if self.field[i][j]:
                    X[i, j] = 0.5
        field = self.figure.get_field()
        for i in range(self.figure.grid_size):
            for j in range(self.figure.grid_size):
                if field[i][j]:
                    X[self.figure.y + i][self.figure.x + j] = 1
        return X.reshape((1, config.HEIGHT * config.WIDTH))