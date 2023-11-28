import pandas as pd
import numpy as np

from preproc_base_data.data import get_data_right,get_data_left

def left_data_add_0(dataframe):
    dataframe['classifier'] = 0
    return dataframe

def right_data_add_0(dataframe):
    dataframe['classifier'] = 1
    return dataframe
