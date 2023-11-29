import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer

from preproc_base_data.pre_proc_pipe import concat_for_pre_built

def vectorise_list(dataframe, max_df=0.9, min_df=0.1, max_features=50):
    #build list for model
    list = dataframe['pre_process_text']

    #instantiate model, use keywords from function
    count_vectorizer = CountVectorizer(max_df = max_df, min_df=min_df, max_features=max_features)

    #fit and transform the data
    X = count_vectorizer.fit_transform(list)
    X = pd.DataFrame(X.toarray(), columns = count_vectorizer.get_feature_names_out(), index = list)

    return X

if __name__ == "__main__":
    print(vectorise_list(concat_for_pre_built()).columns)
    print(vectorise_list(concat_for_pre_built()))
