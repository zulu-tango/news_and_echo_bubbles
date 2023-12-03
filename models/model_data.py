from further_preprocess.lemma import lemmatized_2
from models.vectorisation import count_vectorise
from preproc_base_data.preprocess_pipeline import data_pre_process
import os
import pandas as pd

path = os.getcwd()

def pipeline():
    preprocessed_data = data_pre_process()
    preprocessed_data.to_csv(f'{path}/raw_data/processed_data.csv')
    return preprocessed_data

def embedding():
    dataframe = pd.read_csv(f'{path}/raw_data/processed_data.csv')
    final_preproc = lemmatized_2(dataframe)
    keywords = count_vectorise(final_preproc)
    keywords.to_csv(f'{path}/raw_data/embedded_data.csv')
    return keywords

if __name__ == "__main__":
    print(embedding())
