import pandas as pd
import os

def readCsv(csv):
    csRead = pd.read_csv(os.getcwd() + "/" + csv)
   

def toHotEncode(csv):
    hotEncode = pd.get_dummies(csv)
    #print(hotEncode.head())
