

import pandas as pd
import numpy as np

from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from preproc_base_data.pre_proc_pipe import concat_for_pre_built


def lemma(text):
    noun_lemmatized = [
        WordNetLemmatizer().lemmatize(word, pos = "n") # n --> nouns
        for word in text.split()
        ]
    return ' '.join(noun_lemmatized)

def lemmatized_2(df):
    df['lemmatize'] = df['pre_process_text'].apply(lemma)
    return df
