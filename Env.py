from TetrisGenetic import TetrisGenetic
from Agent import Agent
import config
import algorithm


class Env:
    def __init__(self, Weights=None):
        if Weights:
            self.games = [TetrisGenetic(Agent(weights)) for weights in Weights]
        else:
            self.games = [TetrisGenetic() for i in range(config.NUM_AGENTS)]
        self.over = False
    
    def reset(self):
        self.over = False
        for game in self.games:
            game.reset()
    
    def change_weights(self, weights: list):
        for game, W in zip(self.games, weights):
            game.agent.model = algorithm.build_model()
            game.agent.model.set_weights(W)
    
    def get_population(self):
        return [game.agent for game in self.games]
    
    def iterate(self):
        c = 0
        for game in self.games:
            if not game.game_over:
                game.play()
                c += 1
        if c == 0:
            self.over = True