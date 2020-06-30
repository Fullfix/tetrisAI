from Env import Env
import config
import genetic
import pickle
import matplotlib.pyplot as plt

if config.LOAD_WEIGHTS:
    env = genetic.load_population()
else:
    env = Env()
    with open('scores.txt', 'wb') as f:
        pickle.dump(([], 0), f)

Scores = []
for e in range(1, config.EPOCHS+1):
    while not env.over:
        env.iterate()
    avg_res = genetic.get_avg_res(env.get_population())
    avg_score = genetic.get_avg_score(env.get_population())
    Scores.append(avg_res)
    print(f'avg_res={ avg_res } avg_score={ avg_score } epoch={ e }')
    if config.SAVE and e % config.SAVE_EPOCHS == 0:
        genetic.save_population(env.get_population(), Scores)
        Scores = []
    genetic.generate_next_pop(env)

if config.SAVE:
    genetic.save_population(env.get_population(), Scores)

if config.SHOW:
    S, E = genetic.load_scores()
    plt.plot(E, S)
    plt.show()