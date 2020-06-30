import random
import numpy as np
import config
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam


def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(config.HEIGHT, config.WIDTH, 1)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(len(config.ACTIONS), activation='tanh'),
    ])
    model.compile(optimizer=Adam(lr=config.LEARNING_RATE), loss='mse')
    return model