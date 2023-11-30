import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def count_vectorise(df): #takes the lemmatized column of data
    X = df['lemmatize']
    cv_model = CountVectorizer(max_df= 0.98, max_features= 20_000, min_df= 0.01, ngram_range= (1, 2),stop_words='english')
    word_count_vector=cv_model.fit_transform(X)

    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(word_count_vector)
    feature_names=cv_model.get_feature_names_out()

    tf_idf_vector=tfidf_transformer.transform(cv_model.transform(X))

    results=[]
    for i in range(tf_idf_vector.shape[0]):
        # get vector for a single document
        curr_vector=tf_idf_vector[i]

        #sort the tf-idf vector by descending order of scores
        sorted_items=sort_coo(curr_vector.tocoo())

        #extract only the top n; n here is 10
        keywords=extract_topn_from_vector(feature_names,sorted_items,10)
        results.append(keywords)

    df=pd.DataFrame(zip(X,results),columns=['doc','keywords'])
    return df

def sort_coo(coo_matrix):
    #sorts the values in the vector while preserving the column index
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]

        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]

    return results
