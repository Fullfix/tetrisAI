from Bot import Bot
from Tetris import Tetris
import config
import screen


class Env:
    def __init__(self, show=False):
        self.bot = Bot()
        self.game = Tetris()
        self.show = show
    
    def step(self, action):
        score = self.game.score
        self.game.iteration(config.ACTIONS[action])
        new_score = self.game.score
        reward = new_score - score
        return self.game.get_state(), reward, self.game.game_over
    
    def play_move(self):
        state = self.game.get_state()
        action = self.bot.act(state)
        next_state, reward, done = self.step(action)
        reward = reward if not done else -1
        self.bot.remember(state, action, reward, next_state, done)
        if self.show:
            screen.draw(self.game, tick=False)
        
    
    def play_epoch(self):
        self.game.reset()
        while not self.game.game_over:
            self.play_move()
        if (len(self.bot.memory) > config.BATCH_SIZE):
            self.bot.replay(config.BATCH_SIZE)
        else:
            self.bot.replay(len(self.bot.memory))