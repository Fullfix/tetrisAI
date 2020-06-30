import random
import config
import numpy as np
import algorithm as alg
from Tetris import Tetris


class Agent:
    def __init__(self, weights=None):
        self.totaltime = 0
        self.score = 0
        self.model = alg.build_model()
        if weights:
            self.model.set_weights(weights)
    
    def act(self, state):
        values = self.model.predict(state)
        return config.ACTIONS[np.argmax(values[0])]