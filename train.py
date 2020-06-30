from Env import Env
import config
import genetic

env = Env()

for e in range(config.EPOCHS):
    while not env.over:
        env.iterate()
    avg_score = genetic.get_avg_time(env.get_population())
    print(f'avg_score={ avg_score } epoch={ e }')
    genetic.generate_next_pop(env)