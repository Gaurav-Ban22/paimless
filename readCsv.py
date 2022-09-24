import pandas as pd
import os
import numpy as np

def readCsv(csv):
    csRead = pd.read_csv(os.getcwd() + "/" + csv)
    return csRead
   

def toHotEncodes(csv, output):
    try:
        df = readCsv(csv)
        hotEncode = pd.get_dummies(df[output])
        return np.array(hotEncode)
        #print(hotEncode.head())
    except:
        raise ValueError("bruh u need to actually have that")

#print(toHotEncodes("iris.csv", "variety"))
