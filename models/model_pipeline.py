# import tensorflow as tf
# from tensorflow.keras import optimizers, losses
# from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
# from tensorflow.keras.callbacks import EarlyStopping

import pandas as pd
from preproc_base_data.pre_proc_pipe import concat_for_pre_built
from further_preprocess.lemma import lemmatized_2
from models.vectorisation import count_vectorise

def pipeline():
    preprocessed_data = concat_for_pre_built()
    final_preproc = lemmatized_2(preprocessed_data)
    keywords = count_vectorise(final_preproc)
    ## bert model
    
    return keywords



def search_keyword(df):
    keyword = input('searchword: ')
    returned_articles = []
    for index, row in enumerate(df.keywords):
        if keyword in row:
            returned_articles.append(df['text'][index])
    df = pd.DataFrame(returned_articles,columns=['text','keyword_score'])
    df = df.sort_values(by=['keyword_score'],ascending=False)
    return df[:10]

print(len(search_keyword(pipeline())))
