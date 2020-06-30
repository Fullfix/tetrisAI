from Env import Env
import config
import genetic
import matplotlib.pyplot as plt
env = Env()

Scores = []
Epoches = []
for e in range(config.EPOCHS):
    while not env.over:
        env.iterate()
    avg_res = genetic.get_avg_res(env.get_population())
    avg_score = genetic.get_avg_score(env.get_population())
    Scores.append(avg_res)
    Epoches.append(e+1)
    print(f'avg_res={ avg_res } avg_score={ avg_score } epoch={ e }')
    genetic.generate_next_pop(env)
plt.plot(Epoches, Scores)
plt.show()