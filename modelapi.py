import tensorflow as tf
from tensorflow import keras
import numpy as np

class APIModel():
    def __init__(self, layers, optimizer="rmsprop", loss="binary_crossentropy"):
        self.model = keras.models.Sequential(layers)
        self.optimizer=optimizer
        self.loss = loss

    def predict(self, x):
        return self.model(x)
    
    def train(self, x_train, y_train, batch_size=32, epochs=10):
        self.model.compile(optimizer=self.optimizer, loss=self.loss)
        self.model.fit(x=x_train, y=y_train, batch_size=batch_size, epochs=epochs)