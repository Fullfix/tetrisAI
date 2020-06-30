import random
import config
import numpy as np
import pickle
from deap.tools import cxTwoPoint, cxUniform, cxBlend, mutGaussian
from copy import deepcopy, copy
from Agent import Agent

def eval_agent(agent: Agent):
    return agent.score + 0.05 * agent.totaltime

def mutate(weights: list):
    for W in weights:
        M = np.random.normal(config.MU, config.SIGMA, W.shape)
        P = np.random.choice(2, W.shape, p=[1-config.INDPB, config.INDPB])
        W += M * P