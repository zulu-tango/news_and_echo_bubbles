import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier

def text_vectorise(X):
    #instantiate the TfidVectorizer where we classify words that are not used in 98% of the dataset
    tf_idf_vectorizer = TfidfVectorizer(max_df = 0.98, min_df = 3)
    vectorised_words = pd.DataFrame(tf_idf_vectorizer.fit_transform(X.text).toarray(),
                 columns = tf_idf_vectorizer.get_feature_names_out())
    return vectorised_words

def train_vector_model(X_train, y_train):
    clf = GradientBoostingClassifier(n_estimators=1000, learning_rate=0.1,max_depth=2,random_state=0)
    clf.fit(X_train,y_train)
    return clf
