import pandas as pd
import os

path = os.getcwd()

def get_data():
    data = pd.read_csv(f"{path}/raw_data/friday_data.csv")
    data_2 = pd.read_csv(f'{path}/raw_data/scraped_saturday.csv')
    data_3 = pd.read_csv(f'{path}/raw_data/scraped_data_combined_sunday.csv')
    combined_df = pd.concat([data,data_2,data_3])
    return combined_df

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
