

from ast import fix_missing_locations
from optparse import BadOptionError
import os
from venv import create
import pandas as pd
import readCsv as rc
import modelapi
import templates

import tensorflow
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential
import tkinter as tk

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

finalOut = 0
finalIn = 0
finalPath = ""
finalBatches = 0 
finalEpochs = 0
howManyNeurons = 0
activationFunc = "sigmoid"
outputNeurons = 0
finalColumn = ""
amogus = None

isSimple = True

wind = tk.Tk()
wind.title("Paimless Neural Network Generator")
wind.geometry('500x1000')

def colorize(text, color):
    return color + text + RESET

in_shape, out_shape = None, None
advanced = None
layers = []
apiModel = modelapi.APIModel([])

def switch():
    global isSimple
    isSimple = not isSimple

inputs = tk.Label(wind, text="Input shape (no. of input parameters)?")
inputs.pack()

inputEntry = tk.Entry(wind)
inputEntry.pack()

outputs = tk.Label(wind, text="Output shape (no. of categories)?")
outputs.pack()

outputEntry = tk.Entry(wind)
outputEntry.pack()

dropDownt = tk.Label(wind, text="Do you want to use a simple or advanced model? (true = yes, false = no)")
dropDownt.pack()

zo = ["True", "False"]
amogus = tk.StringVar(wind, "true")
dropDown = tk.OptionMenu(wind, amogus, *zo)
dropDown.pack()

patho = tk.Label(wind, text="Path to csv: ")
patho.pack()

pathoText = tk.Entry(wind)
pathoText.pack()

op = tk.Label(wind, text="Output column: ")
op.pack()

opt = tk.Entry(wind)
opt.pack()

bat = tk.Label(wind, text="Batches: ")
bat.pack()

bate = tk.Entry(wind)
bate.pack()

epo = tk.Label(wind, text="Epoch #: ")
epo.pack()

epoe = tk.Entry(wind)
epoe.pack()

howMany = tk.Label(wind, text="How many hidden layers?")
howMany.pack()
howManyText = tk.Entry(wind)
howManyText.pack()

act = tk.Label(wind, text="Activation function: ")
act.pack()

acte = tk.Entry(wind)
acte.pack()


outN = tk.Label(wind, text="How many output neurons")
outN.pack()

outNT = tk.Entry(wind)
outNT.pack()

def turnIntoServer():
    os.system("cd saveData && python3 -m httpServer.py 8000")


def createWindow():
    window = tk.Toplevel(wind)
    window.title("Advanced")
    window.geometry("500x500")
    window.grab_set()

    btnp = tk.Button(window, text = 'Turn into server?', bd = '10', command=turnIntoServer)
    btnp.pack()

def finish():
    global finalOut, finalIn, finalPath, finalBatches, finalEpochs, howManyNeurons, activationFunc, outputNeurons, finalColumn, in_shape, out_shape, advanced, layers, apiModel, isSimple, amogus
    finalOut = outputEntry.get()
    finalIn = inputEntry.get()
    finalPath = pathoText.get()
    finalBatches = bate.get()
    finalEpochs = epoe.get()
    howManyNeurons = howManyText.get()
    activationFunc = acte.get()
    finalColumn = opt.get()
    isSimple = bool(amogus.get())
    outputNeurons = outNT.get()
    

    def setIO():
        global in_shape, out_shape  
        in_shape = int(finalIn)
        out_shape = int(finalOut)

    def mainLoop():
        global apiModel, advanced
        name = "model"
        if(in_shape == None or out_shape == None):
            setIO()
        if(advanced == None):
            advanced = False
        if(advanced == True):
            layers.append(Input(in_shape))


        if(advanced):
            action = int(howManyNeurons)
            if(action > 0):
                out_neurons = int(outputNeurons)
                activation = activationFunc            
                layers.append(Dense(out_neurons, activation=activation))
                mainLoop()
            if(action <= 0):
                layers.append(Dense(out_shape, activation="sigmoid"))
                apiModel.model = Sequential(layers) 
        else:
            
            if(isSimple):
                apiModel.model = templates.classifier_small(in_shape, out_shape)
            if(not isSimple):
                apiModel.model = templates.classifier_large(in_shape, out_shape)


    mainLoop()

    x_train, y_train = None, None

    def csvProcess():
        global x_train, y_train
        path = finalPath
        out = finalColumn
        print(colorize(path, RED))
        print(colorize(out, RED))

        y_train = rc.toHotEncodes(path, out)
        x_train = rc.readInputs(path, out)


    csvProcess()

    def train():
        global x_train, y_train
        #if(advanced):
        batch_size = int(finalBatches)
        epochs = int(finalEpochs)

        apiModel.train(x_train, y_train, batch_size=batch_size, epochs=epochs)
        print("training done")

    train()
    print("training done")

    co = os.listdir(os.getcwd() + "/" + "saveData")

    for i in co:
        if i != "httpServer.py":
            os.remove(os.getcwd()+"/"+"saveData/"+i)
                
    apiModel.model.save("saveData/model.h5")

    createWindow()


    

    # def secure():
    #     whether = input("Do you want to host this on a semisecure webserver? Press ctrl-c to stop hosting when you're done. (y/n) ")
    #     if whether == "y":
    #         os.system("cd saveData && python3 -m httpServer.py 8000")
    #     if whether == "n":
    #         print("rip")
    #     else:
    #         print("invalid input")
    #         secure()

    # secure()


def setAdvanced():
    widgets = {}
    advanced = True
    for widget in wind.winfo_children():
        widget.destroy()

    def addAnother():
        def delete(object, objecttwo):
            object.destroy()
            objecttwo.destroy()
            if len(widgets) > 0:
                widgets.popitem()

        if len(widgets) < 9:
            widget = tk.Entry(wind)
            widget.pack()
            widgettwo = tk.Button(wind, text="Delete")
            widgettwo.pack()
            widgets[widget] = widgettwo
            widgettwo.configure(command=lambda: delete(widget, widgettwo))
            print(widgets)


    finalBtn = tk.Button(wind, text="Generate")
    finalBtn.pack()



    inputs = tk.Label(wind, text="Input shape (no. of input parameters)?")
    inputs.pack()

    inputEntry = tk.Entry(wind)
    inputEntry.pack()

    outputs = tk.Label(wind, text="Output shape (no. of categories)?")
    outputs.pack()

    outputEntry = tk.Entry(wind)
    outputEntry.pack()

    patho = tk.Label(wind, text="Path to csv: ")
    patho.pack()

    pathoText = tk.Entry(wind)
    pathoText.pack()

    op = tk.Label(wind, text="Output column: ")
    op.pack()

    opt = tk.Entry(wind)
    opt.pack()

    bat = tk.Label(wind, text="Batches: ")
    bat.pack()

    bate = tk.Entry(wind)
    bate.pack()

    epo = tk.Label(wind, text="Epoch #: ")
    epo.pack()

    epoe = tk.Entry(wind)
    epoe.pack()

    howMany = tk.Label(wind, text="How many hidden layers?")
    howMany.pack()

    addMore = tk.Button(wind, text="Add hidden layer", bd = 6, command=addAnother)
    addMore.pack()

    howManyText = tk.Entry(wind)
    howManyText.pack()

    act = tk.Label(wind, text="Activation function: ")
    act.pack()

    acte = tk.Entry(wind)
    acte.pack()


    outN = tk.Label(wind, text="How many output neurons")
    outN.pack()

    outNT = tk.Entry(wind)
    outNT.pack()

    

    

    def finisha():
        global finalOut, finalIn, finalPath, finalBatches, finalEpochs, howManyNeurons, activationFunc, outputNeurons, finalColumn, in_shape, out_shape, advanced, layers, apiModel 
        
        finalOut = outputEntry.get()
        finalIn = inputEntry.get()
        finalPath = pathoText.get()
        finalBatches = bate.get()
        finalEpochs = epoe.get()
        howManyNeurons = howManyText.get()
        activationFunc = acte.get()
        finalColumn = opt.get()
        outputNeurons = outNT.get()

        

        def setIO():
            global in_shape, out_shape  
            in_shape = int(finalIn)
            out_shape = int(finalOut)

        def mainLoop():
            global apiModel, advanced
            name = "model"
            if(in_shape == None or out_shape == None):
                setIO()
            if(advanced == None):
                advanced = False
            if(advanced == True):
                layers.append(Input(in_shape))


            if(advanced):
                action = int(howManyNeurons)
                if(len(widgets) > 0):
                    
                    activation = activationFunc            
                    for i in range(len(widgets)):
                        out_neurons = widgets.ElementAt(i).key.get()
                        layers.append(Dense(out_neurons, activation=activation))
                    mainLoop()
                if(len(widgets) <= 0):
                    layers.append(Dense(out_shape, activation="sigmoid"))
                    apiModel.model = Sequential(layers) 
            else:
                
                if(isSimple):
                    apiModel.model = templates.classifier_small(in_shape, out_shape)
                if(not isSimple):
                    apiModel.model = templates.classifier_large(in_shape, out_shape)

        
        mainLoop()
        

        x_train, y_train = None, None

        def csvProcess():
            global x_train, y_train
            path = finalPath
            out = finalColumn
            print(colorize(path, RED))
            print(colorize(out, RED))

            y_train = rc.toHotEncodes(path, out)
            x_train = rc.readInputs(path, out)


        csvProcess()

        def train():
            global x_train, y_train
            #if(advanced):
            batch_size = int(finalBatches)
            epochs = int(finalEpochs)

            apiModel.train(x_train, y_train, batch_size=batch_size, epochs=epochs)
            print("training done")

        train()
        print("training done")

        co = os.listdir(os.getcwd() + "/" + "saveData")

        for i in co:
            if i != "httpServer.py" and i != "__pycache__":
                os.remove(os.getcwd()+"/"+"saveData/"+i)
                    
        apiModel.model.save("saveData/model.h5")

        createWindow()

    finalBtn.configure(command=finisha)

        


        

        # def secure():
        #     whether = input("Do you want to host this on a semisecure webserver? Press ctrl-c to stop hosting when you're done. (y/n) ")
        #     if whether == "y":
        #         os.system("cd saveData && python3 -m httpServer.py 8000")
        #     if whether == "n":
        #         print("rip")
        #     else:
        #         print("invalid input")
        #         secure()

        # secure()

    



btn = tk.Button(wind, text = 'Make Advanced?', bd = '5', command=setAdvanced)
btn.pack()



finalBtn = tk.Button(wind, text="Generate", command=finish)
finalBtn.pack()






wind.mainloop()


        





