

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import pandas as pd
import readCsv as rc
import modelapi
import templates
import tensorflow
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential

RESET = "\u001B[0m"
BLACK = "\u001B[30m"
RED = "\u001B[31m"
GREEN = "\u001B[32m"
YELLOW = "\u001B[33m"
BLUE = "\u001B[34m"
PURPLE = "\u001B[35m"
CYAN = "\u001B[36m"
WHITE = "\u001B[37m"
BLACK_BOLD = "\033[1;30m"
RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
BLUE_BOLD = "\033[1;34m"
PURPLE_BOLD = "\033[1;35m"
CYAN_BOLD = "\033[1;36m"
WHITE_BOLD = "\033[1;37m"


def colorize(text, color):
    return color + text + RESET

in_shape, out_shape = None, None
advanced = None
layers = []
apiModel = modelapi.APIModel([])

def setIO():
    global in_shape, out_shape
    in_shape = int(input("input shape (no. of input parameters)?"))
    out_shape = int(input("output shape (no. of categories)?"))


def mainLoop():
    global apiModel, advanced
    name = "model"
    if(in_shape == None or out_shape == None):
        setIO()
    if(advanced == None):
        x = input("Advanced mode? (0 for advanced, 1 for beginner mode) (advanced lets you make your own model)")
        if(x == "1"):
            advanced = False
        else:
            advanced = True
            layers.append(Input(in_shape))

    if(advanced):
        action = input("[a]dd hidden layer, [b]egin")
        if(action == "a"):
            out_neurons = int(input("output neurons?"))
            activation = input("activation function?")            
            layers.append(Dense(out_neurons, activation=activation))
            mainLoop()
        if(action == "b"):
            layers.append(Dense(out_shape, activation="sigmoid"))
            apiModel.model = Sequential(layers)
    else:
        print("what template do you want to use? (classifier_small[1], classifier_large[2])")
        template = input()
        if(template == "1"):
            apiModel.model = templates.classifier_small(in_shape, out_shape)
        if(template == "2"):
            apiModel.model = templates.classifier_large(in_shape, out_shape)


mainLoop()

x_train, y_train = None, None

def csvProcess():
    global x_train, y_train
    path = input("path to csv: ")
    out = input("output column in csv: ")

    y_train = rc.toHotEncodes(path, out)
    x_train = rc.readInputs(path, out)


csvProcess()

def train():
    #if(advanced):
    batch_size = int(input("batch size: "))
    epochs = int(input("epochs (number of iterations on one dataset): "))

    apiModel.train(x_train, y_train, batch_size=batch_size, epochs=epochs)

train()
apiModel.model.save("saveData/model.h5")

def secure():
    whether = input("Do you want to host this on a semisecure webserver? Press ctrl-c to stop hosting when you're done. (y/n) ")
    if whether == "y":
        os.system("cd saveData && python3 -m httpServer.py 8000")
    if whether == "n":
        print("rip")
    else:
        print("invalid input")
        secure()

secure()