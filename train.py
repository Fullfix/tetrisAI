from Env import Env

env = Env(show=True)

for e in range(10000):
    env.play_epoch()
    print(env.game.score, env.bot.epsilon)