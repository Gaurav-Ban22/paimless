import tensorflow as tf
from tensorflow import keras

class APIModel(keras.models.Model):
    def __init__(self, layers):
        self.layers = layers

    def predict(self, x):
        for i in range(len(layers)):
            x = layers[i](x)
        return x
    
    def train(self, x_train, y_train):
        