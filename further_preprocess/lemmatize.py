import pandas as pd
import numpy as np

from nltk.corpus import wordnet as wn

from preproc_base_data.pre_proc_pipe import concat_for_pre_built

def lemmatize_func(dataframe):
    #instantiate lemmatizer model
    from nltk.stem import WordNetLemmatizer
    lemmatize_model = WordNetLemmatizer()

    #make a list of lists for lemmatizer
    empty_list_2 = []
    for text in dataframe['pre_process_text']:
        empty_list_1 = []
        empty_list_1.append(text.split())
        # print(empty_list_1)
        empty_list_2.append(empty_list_1[0])

    #test stage print function
    # print(len(empty_list_2))

    #lemmatize VERBS
    empty_list_4 = []
    for article in empty_list_2:
        # print(article)
        empty_list_3 = []
        for words in article:
            lemm_word = lemmatize_model.lemmatize(words, pos = "v")
            empty_list_3.append(lemm_word)
        empty_list_4.append(empty_list_3)

    #lemmatize NOUNS
    empty_list_6 = []
    for article in empty_list_4:
        # print(article)
        empty_list_5 = []
        for words in article:
            lemm_word = lemmatize_model.lemmatize(words, pos = "n")
            empty_list_5.append(lemm_word)
        empty_list_6.append(empty_list_5)

    #add into dataframe
    dataframe['pre_process_text'] = empty_list_6

    return dataframe

if __name__ == "__main__":
    print(lemmatize_func(concat_for_pre_built()))
    # print(concat_for_pre_built()['pre_process_text'][0])
