from further_preprocess.lemma import lemmatized_2
from models.vectorisation import count_vectorise
from preproc_base_data.preprocess_pipeline import data_pre_process


def pipeline():
    preprocessed_data = data_pre_process()
    return preprocessed_data

def embedding():
    dataframe = pipeline()
    final_preproc = lemmatized_2(dataframe)
    keywords = count_vectorise(final_preproc)
    return keywords

if __name__ == "__main__":
    print(embedding())
