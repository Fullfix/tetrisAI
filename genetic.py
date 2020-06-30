import random
import config
import numpy as np
import time
import pickle
import keras
from deap.tools import cxTwoPoint, cxUniform, cxBlend, mutGaussian
from copy import deepcopy, copy
from Agent import Agent
from Env import Env

def eval_agent(agent: Agent):
    return agent.score + 0.005 * agent.totaltime

def mutate(weights: list):
    for W in weights:
        M = np.random.normal(config.MU, config.SIGMA, W.shape)
        P = np.random.choice(2, W.shape, p=[1-config.INDPB, config.INDPB])
        W += M * P

def choose_best(population: list, n: int):
    l = config.NUM_AGENTS
    sorted_pop = sorted(population, key=eval_agent, reverse=True)
    sorted_pop = [x.model.get_weights() for x in sorted_pop]
    return sorted_pop[:n], sorted_pop[n:l-n], sorted_pop[l-n:]

def get_avg_res(population: list):
    return sum(list(map(eval_agent, population))) / len(population)

def get_avg_score(population: list):
    return sum(list(map(lambda x: x.score, population))) / len(population)

def generate_next_pop(env: Env):
    # choose best agents
    t = time.time()
    population = env.get_population()
    bestpopulaton, middle, worst = choose_best(population, config.BEST_IND_NUM)
    # crossover middle
    for i in range(0, len(middle), 2):
        middle[i], middle[i+1] = cxBlend(middle[i], middle[i+1], config.ALPHA)
    newpopulation = bestpopulaton + middle + deepcopy(bestpopulaton)
    # mutate
    for weights in newpopulation:
        mutate(weights)
    # needed to optimize time
    keras.backend.clear_session()
    # set weights
    env.change_weights(newpopulation)
    env.reset()

def save_scores(Scores: list):
    with open('scores.txt', 'rb') as f:
        S, E = pickle.load(f)
    if E != 0:
        S += Scores
        E = len(S)
    else:
        E = len(Scores)
        S = Scores
    with open('scores.txt', 'wb') as f:
        pickle.dump((S, E), f)

def load_scores():
    with open('scores.txt', 'rb') as f:
        S, E = pickle.load(f)
    return S, range(1, E+1)
    

def save_population(population: list, Scores: list):
    Weights = list(map(lambda x: x.model.get_weights(), population))
    with open('weights.txt', 'wb') as f:
        pickle.dump(Weights, f)
    save_scores(Scores)
    print('saved')

def load_population():
    with open('weights.txt', 'rb') as f:
        Weights = pickle.load(f)
    env = Env(Weights)
    print('loaded')
    return env