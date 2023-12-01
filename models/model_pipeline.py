import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
from preproc_base_data.pre_proc_pipe import data_pre_proc
from further_preprocess.lemma import lemmatized_2
from models.vectorisation import count_vectorise
from models.ideology_model import full_ideology_model, ideology_model_predictor,instantiate_tokenizer, text_tokenizer
from models.n_class_ideology_model import full_n_class_ideology_model,top_class
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification


IM_TOKEN_MAX_LEN = int(os.environ.get('IM_TOKEN_MAX_LEN'))

def pipeline():
    preprocessed_data = data_pre_proc()
    return preprocessed_data

def sentiment_model_train():
    output = full_ideology_model(pipeline())
    return output

def embedding():
    final_preproc = lemmatized_2(pipeline())
    keywords = count_vectorise(final_preproc)
    return keywords

def sentiment_model_5():
    output = full_n_class_ideology_model(pipeline(),n=5)
    return output

def sentiment_predict():
    df = embedding() ## need to run it on test data
    X = df["pre_process_text"].tolist()
    tokens = text_tokenizer(X,
                   instantiate_tokenizer(),
                   max_len = IM_TOKEN_MAX_LEN,
                   truncation = True,
                   padding = "max_length")
    # output_scores = ideology_model_predictor(load_model('sentiment_model_01_12_2023_15_09_36/'),tokens)
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained('sentiment_model_friday_5')
    scores = ideology_model_predictor(loaded_model,tokens)
    top_class_list = top_class(scores)
    df['pred_class'] = top_class_list
    return df

def search_keyword(df):
    keyword = input('searchword: ')
    returned_articles = []
    for index, row in enumerate(df.keywords):
        if keyword in row:
            returned_articles.append((df['text'][index],df['urls'][index],df['keywords'][index][keyword],df['pred_class'][index]))
    df = pd.DataFrame(returned_articles,columns=['text','keyword_score','pred_class'])
    df = df.sort_values(by=['keyword_score'],ascending=False)
    return df[:10]

print(search_keyword(sentiment_predict()))
#print(pipeline())
