import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd

from models.ideology_model import full_ideology_model, ideology_model_predictor,instantiate_tokenizer, text_tokenizer
from models.n_class_ideology_model import full_n_class_ideology_model,top_class
from models.model_data import pipeline, embedding
from transformers import TFDistilBertForSequenceClassification

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
    df = pd.read_csv(f'{path}/raw_data/embedded_data.csv')
    X = df["pre_process_text"].tolist()
    tokens = text_tokenizer(X,
                   instantiate_tokenizer(),
                   max_len = IM_TOKEN_MAX_LEN,
                   truncation = True,
                   padding = "max_length")
    # output_scores = ideology_model_predictor(load_model('sentiment_model_01_12_2023_15_09_36/'),tokens)
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained('sentiment_model_saturday_5')
    scores = ideology_model_predictor(loaded_model,tokens)
    top_class_list = top_class(scores)
    df['pred_class'] = top_class_list

    df.to_csv(f'{path}/raw_data/predicted_sentiment.csv')
    #concat new data every day
    return df

## add function to return different bias articles

if __name__ == "__main__":
    #print(sentiment_model_5())
    print(sentiment_predict())
