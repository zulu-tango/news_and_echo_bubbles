import pandas as pd
import numpy as np
from preproc_base_data.manual_pre_proc import manual_pre_process, base_author_col_add, fix_text_characters
from preproc_base_data.score import right_data_add_0, left_data_add_0
from preproc_base_data.data import get_data_left, get_data_right
from preproc_base_data.data import text_for_pre_built_pre_proc



#Combined preproc function

def left_pipe_pre_proc():
    data = get_data_left()
    df_0 = left_data_add_0(dataframe=data)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

def right_pipe_pre_proc():
    data = get_data_right()
    df_0 = right_data_add_0(dataframe=data)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

def join_dataframes(dataframe_1, dataframe_2):
    df_concat = dataframe_1.merge(dataframe_2,how='outer')
    # df_concat =df_concat.reset_index(drop=True)
    return df_concat

#Combined pipe to be ready for pre built online transformers
def pipe_for_pre_made_transformer_left():
    data = get_data_left()
    df_1 = left_data_add_0(dataframe=data)
    df_2 = text_for_pre_built_pre_proc(dataframe=df_1)
    return df_2

def pipe_for_pre_made_transformer_right():
    data = get_data_right()
    df_1 = right_data_add_0(dataframe=data)
    df_2 = text_for_pre_built_pre_proc(dataframe=df_1)
    return df_2

def concat_for_pre_built():
    df_left = left_pipe_pre_proc()
    df_right = right_pipe_pre_proc()
    combined_df = join_dataframes(dataframe_1=df_left,dataframe_2=df_right)
    return combined_df
