import pandas as pd
import os

path = os.getcwd()

def get_data_right():
    brainded_right = pd.read_csv(f"{path}/raw_data/braindedright.csv")
    return brainded_right

def get_data_left():
    brainded_left = pd.read_csv(f"{path}/raw_data/braindedleft.csv")
    return brainded_left
