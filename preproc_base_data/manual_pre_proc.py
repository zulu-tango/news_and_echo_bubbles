import pandas as pd
from urllib.parse import urlparse



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

def add_pre_proc_text(dataframe):
    # import string for punctuation library
    import string

    #start a list, equal to lwoer case of text column of dataframe.
    i = 0
    new_list = []
    for text in brainded_left['pre_process_text']:
        new_list.append(brainded_left['pre_process_text'][i].lower())
        i += 1

    #remove special characters and http "\n" items.
    second_list = []
    for text in new_list:
        for special in string.punctuation:
            text = text.replace(special, ' ')
        text = text.replace('\n', ' ')
    second_list.append(text)

    #change dataframe column to equal finalised adjusted list
    dataframe["pre_process_text"] = second_list

    return dataframe


#Combined preproc function

def pipe_pre_proc(dataframe):
    df_1 = manual_pre_process(dataframe=dataframe)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = add_pre_proc_text(dataframe=df_2)
    return df_3
