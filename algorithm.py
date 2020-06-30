import random
import numpy as np
import tensorflow as tf
import config
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam


def build_model():
    model = Sequential([
        Dense(32, activation='relu', input_shape=(config.HEIGHT*config.WIDTH,)),
        Dense(16, activation='relu'),
        Dense(len(config.ACTIONS), activation='tanh'),
    ])
    model.compile(optimizer=Adam(lr=0.001), loss='mse')
    return model