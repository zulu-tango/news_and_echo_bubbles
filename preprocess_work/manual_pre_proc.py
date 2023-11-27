import pandas as pd
from urllib.parse import urlparse

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

def source_from_base_webpage(dataframe):
    #import library in function when called in case not installed or used in the file
    from urllib.parse import urlparse

    #check variety of news sources in each dataset
    urls_right = [urlparse(dataframe.link[row]).netloc for row in range(len(dataframe.link))]
    dataframe['urls'] = urls_right

    return dataframe

