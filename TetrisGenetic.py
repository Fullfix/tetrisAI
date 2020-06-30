from Tetris import Tetris
from Agent import Agent


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