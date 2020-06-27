import numpy as np
import random
from collections import deque
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from keras.optimizers import Adam
import config


class Bot:
    def __init__(self):
        self.state_size = config.WIDTH * config.HEIGHT
        self.memory = deque(maxlen=2000)
        self.gamma = config.GAMMA
        self.epsilon = config.EPSILON
        self.epsilon_decay = config.EPSILON_DECAY
        self.epsilon_min = config.EPSILON_MIN
        self.learning_rate = config.LEARNING_RATE
        self.model = self.build_model()
    
    def build_model(self):
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
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append([state, action, reward, next_state, done])
    
    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(range(len(config.ACTIONS)))
        values = self.model.predict(state)
        return np.argmax(values[0])
    
    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
        
        self.model.fit(state, target_f, epochs=5, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
    
    def load(self, name):
        self.model.load_weights(name)
    
    def save(self, name):
        self.model.save_weights(name)