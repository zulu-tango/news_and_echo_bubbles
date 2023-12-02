from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

def lemma(text):
    noun_lemmatized = [
        WordNetLemmatizer().lemmatize(word, pos = "n") # n --> nouns
        for word in text.split()
        ]
    return ' '.join(noun_lemmatized)

def lemmatized_2(df):
    df['lemmatize'] = df['pre_processed_data'].apply(lemma)
    return df
