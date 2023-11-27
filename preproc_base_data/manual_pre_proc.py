import pandas as pd
from urllib.parse import urlparse

from preproc_base_data.data import get_data_left

"""
    Multiple functions below to clean data, the pipe_pre_proc function combines them all
    together, see bottom of document
"""

def manual_pre_process(dataframe):
    #convert date+time column into separate columns
    dataframe[['pdate','time']] = dataframe['pdate'].str.split(' ', n=1, expand=True)
    dataframe['pdate'] = pd.to_datetime(dataframe['pdate'])

    #make dates all within 15 months, remove outliers
    mask = dataframe['pdate'] > '2020-01-01'
    dataframe = dataframe[mask].reset_index()

    #drop N/As from the dataframe
    dataframe = dataframe.dropna().reset_index()

    #check amount of data in each dataset that is relevant
    print(f'processed data: {dataframe.title.count()}')

    return dataframe

def base_author_col_add(dataframe):
    #import library in function when called in case not installed or used in the file
    from urllib.parse import urlparse

    #check variety of news sources in each dataset
    urls_right = [urlparse(dataframe.link[row]).netloc for row in range(len(dataframe.link))]
    dataframe['urls'] = urls_right

    return dataframe

def fix_text_characters(dataframe):
    #make a copy of text
    dataframe['pre_process_text'] = dataframe['text']

    #convert to lower
    dataframe['pre_process_text'] = dataframe['pre_process_text'].astype('str')
    i = 0
    new_list = []
    for text in dataframe['pre_process_text']:
        # text = str(text)
        new_list.append(dataframe['pre_process_text'][i].lower())
        i += 1
    dataframe['pre_process_text'] = new_list

    # import string library in function, assume slow but avoid errors
    import string
    second_list = []
    for text in dataframe['pre_process_text']:
        for special in string.punctuation:
            text = text.replace(special, ' ')
        text = text.replace('\n', ' ')
        second_list.append(text)

    dataframe['pre_process_text'] = second_list
    return dataframe

def just_text_for_hug_face(dataframe):
    #filter just text column for now, can add more as we need.
    df_1 = dataframe['text']
    return df_1


#Combined preproc function

def pipe_pre_proc(dataframe):
    df_1 = manual_pre_process(dataframe=dataframe)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

print(pipe_pre_proc(get_data_left()))


