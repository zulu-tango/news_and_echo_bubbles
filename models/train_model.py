import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd

from models.ideology_model import full_ideology_model, ideology_model_predictor,instantiate_tokenizer, text_tokenizer
from models.n_class_ideology_model import full_n_class_ideology_model,top_class
from models.model_data import pipeline, embedding
from transformers import TFDistilBertForSequenceClassification
from datetime import date, timedelta

IM_TOKEN_MAX_LEN = int(os.environ.get('IM_TOKEN_MAX_LEN'))
path = os.getcwd()

def sentiment_model_train():
    output = full_ideology_model(pipeline())
    return output

def sentiment_model_5():
    output = full_n_class_ideology_model(pipeline(),n=5)
    print('model trained')
    return output

def sentiment_predict():
    df = embedding()
    X = df["pre_process_text"].tolist()
    tokens = text_tokenizer(X,
                   instantiate_tokenizer(),
                   max_len = IM_TOKEN_MAX_LEN,
                   truncation = True,
                   padding = "max_length")
    # output_scores = ideology_model_predictor(load_model('sentiment_model_01_12_2023_15_09_36/'),tokens)
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained('sentiment_model_monday')
    scores = ideology_model_predictor(loaded_model,tokens)
    top_class_list = top_class(scores)
    df['pred_class'] = top_class_list
    df = df[['link','pdate','title','author','text','article_length','urls','pre_process_text','5_step_classifier','lemmatize','keywords','pred_class']] #add summarise column

    yesterday = date.today() - timedelta(days=1)

    existing_df = pd.read_csv(f'{path}/raw_data/base_table_{yesterday}_stopwords_3.csv')
    updated_df = pd.concat([existing_df,df],axis=0)
    updated_df = updated_df[['link','pdate','title','author','text','article_length','urls','pre_process_text','5_step_classifier','lemmatize','keywords','pred_class']]
    updated_df.drop_duplicates(subset='title',inplace=True,keep='first')
    updated_df.reset_index(drop=True,inplace=True)
    updated_df.to_csv(f"{path}/raw_data/base_table_{date.today()}.csv")

    return updated_df

## add column for summarising

if __name__ == "__main__":
    #print(sentiment_model_5())
    print(sentiment_predict())
