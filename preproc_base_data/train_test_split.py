from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def shuffle_data(dataframe):
    df = dataframe.sample(frac=1).reset_index(drop=True)
    return df

def train_test_split(dataframe):
    #import within function to avoid errors
    from sklearn.model_selection import train_test_split

    #shuffle dataset (!!!! using shuffle key word arguement in train_test_split)
    # df = dataframe.sample(frac=1).reset_index(drop=True)

    #create X and y
    X = dataframe[['pre_process_text']]
    y = dataframe['classifier']

    #instantiate model
    X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.7, random_state=0,shuffle=True)

    return X_train, X_test, y_train, y_test
