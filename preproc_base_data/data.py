import pandas as pd
import os

path = os.getcwd()

def get_data_right():
    brainded_right = pd.read_csv(f"{path}/raw_data/braindedright.csv")
    return brainded_right

def get_data_left():
    brainded_left = pd.read_csv(f"{path}/raw_data/braindedleft.csv")
    return brainded_left

def text_for_pre_built_pre_proc(dataframe):
    dataframe['text'] = dataframe['text'].astype('str')
    df_1 = dataframe['text']
    return df_1
