import pandas as pd
import os
import numpy as np

def readCsv(csv):
    csRead = pd.read_csv(os.getcwd() + "/" + csv)
   

def toHotEncodes(csv):
    hotEncode = pd.get_dummies(csv)
    return np.array(hotEncode)
    #print(hotEncode.head())
