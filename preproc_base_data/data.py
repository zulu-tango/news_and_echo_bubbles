import pandas as pd
import os

path = os.getcwd()

def get_data():
    data = pd.read_csv(f"{path}/raw_data/friday_data.csv")
    return data

def get_data_right():
    brainded_right = pd.read_csv(f"{path}/raw_data/braindedright.csv")
    return brainded_right

def get_data_left():
    brainded_left = pd.read_csv(f"{path}/raw_data/braindedleft.csv")
    return brainded_left

def get_data_generic(csv_name="braindedright"):
    data = pd.read_csv(f"{path}/raw_data/{csv_name}.csv")
    return data

def text_for_pre_built_pre_proc(dataframe):
    df_1 = dataframe[['text','classifier']].astype('str')
    # df_1 = dataframe[['text']]
    return df_1


if __name__ == "__main__":
    print(get_data_left())
