import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import pandas as pd
from preproc_base_data.pre_proc_pipe import concat_for_pre_built
from further_preprocess.lemma import lemmatized_2
from models.vectorisation import count_vectorise
from models.ideology_model import full_ideology_model, ideology_model_predictor,instantiate_tokenizer, text_tokenizer, tf_dataset_constructor
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification


IM_TOKEN_MAX_LEN = int(os.environ.get('IM_TOKEN_MAX_LEN'))

def pipeline():
    preprocessed_data = concat_for_pre_built()
    final_preproc = lemmatized_2(preprocessed_data)
    keywords = count_vectorise(final_preproc)
    return keywords

def sentiment_model_train():
    output = full_ideology_model(pipeline())
    return output

def sentiment_predict():
    df = pipeline() ## need to run it on test data
    X = df["pre_process_text"].tolist()
    tokens = text_tokenizer(X,
                   instantiate_tokenizer(),
                   max_len = IM_TOKEN_MAX_LEN,
                   truncation = True,
                   padding = "max_length")
    # output_scores = ideology_model_predictor(load_model('sentiment_model_01_12_2023_15_09_36/'),tokens)
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained('sentiment_model_01_12_2023_15_09_36/')
    scores = ideology_model_predictor(loaded_model,tokens)
    df['pred_probas'] = scores[:,1]
    return df

def search_keyword(df):
    keyword = input('searchword: ')
    returned_articles = []
    for index, row in enumerate(df.keywords):
        if keyword in row:
            returned_articles.append((df['text'][index],df['urls'][index],df['keywords'][index][keyword],df['pred_probas'][index]))
    df = pd.DataFrame(returned_articles,columns=['text','keyword_score','pred_probas'])
    df = df.sort_values(by=['keyword_score'],ascending=False)
    return df[:10]

#print(search_keyword(sentiment_model_train()))
print(search_keyword(sentiment_predict()))
