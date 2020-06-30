from Env import Env
import config

env = Env()

for e in range():
    env.play_epoch(config.EPOCHS)
    print(f'score={env.game.score}, eps={env.bot.epsilon}, epoch={e}')