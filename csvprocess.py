import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def process_csv_onehot(path, input_cols, output_col):
    df = pd.read_csv(path)
    y_train = df.columns[output_col]
    print(y_train)

    
