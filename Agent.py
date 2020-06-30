import random
import config
import numpy as np
import algorithm as alg
from Tetris import Tetris


class Agent:
    def __init__(self, weights=None):
        self.model = alg.build_model()
        if weights:
            self.model.load_weights(weights)
    
    def act(self, state):
        values = self.model.predict(state)
        return config.ACTIONS[np.argmax(values[0])]
    
    def load(self, name):
        self.model.load_weights(name)
    
    def save(self, name):
        self.model.save_weights(name)