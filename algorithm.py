import random
import numpy as np
import tensorflow as tf
import config
import time
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam


def build_model_conv():
    model = Sequential([
        Conv2D(32, (3, 3), input_shape=(config.HEIGHT, config.WIDTH, 1), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(16, activation='relu'),
        Dense(len(config.ACTIONS), activation='tanh'),
    ])
    model.compile(optimizer=Adam(lr=0.001), loss='mse')
    return model

def build_model():
    model = Sequential([
        Dense(32, activation='relu', input_shape=(config.HEIGHT * config.WIDTH,)),
        Dense(16, activation='relu'),
        Dense(len(config.ACTIONS), activation='tanh'),
    ])
    model.compile(optimizer=Adam(lr=0.001), loss='mse')
    return model