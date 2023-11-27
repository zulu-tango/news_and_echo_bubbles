import pandas as pd
import numpy as np
from preproc_base_data.manual_pre_proc import manual_pre_process, base_author_col_add, fix_text_characters
from preproc_base_data.score import right_data_add_0, left_data_add_0
from preproc_base_data.data import get_data_left, get_data_right



#Combined preproc function

def left_pipe_pre_proc(dataframe):
    df_0 = left_data_add_0(dataframe=dataframe)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

def right_pipe_pre_proc(dataframe):
    df_0 = right_data_add_0(dataframe=dataframe)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

def join_dataframes(dataframe_1, dataframe_2):
    df_concat = pd.concat([dataframe_1,dataframe_2])
    return df_concat

# print(left_pipe_pre_proc(get_data_left())['binary'])

# print(join_dataframes(left_pipe_pre_proc(get_data_left()), right_pipe_pre_proc(get_data_right())))
