import pandas as pd
from urllib.parse import urlparse

from preproc_base_data.data import get_data_left

"""
    Multiple functions below to clean data, the pipe_pre_proc function combines them all
    together, see python file named pre_proc_pipe
"""

def manual_pre_process_2(dataframe):
    #convert date+time column into separate columns
    dataframe[['pdate','time']] = dataframe['pdate'].str.split(' ', n=1, expand=True)
    dataframe['pdate'] = pd.to_datetime(dataframe['pdate'])

    #check amount of data in each dataset that is relevant
    #print(f'processed data: {dataframe.title.count()}')

    return dataframe

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
    #print(f'processed data: {dataframe.title.count()}')

    return dataframe

def base_author_col_add(dataframe):
    #import library in function when called in case not installed or used in the file
    from urllib.parse import urlparse

    #check variety of news sources in each dataset
    urls_right = [urlparse(dataframe.link[row]).netloc for row in range(len(dataframe.link))]
    dataframe['urls'] = urls_right

    return dataframe

def fix_text_characters(dataframe):
    import pandas as pd
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
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for text in dataframe['pre_process_text']:
        for special in punc:
            text = text.replace(special, ' ')
        text = text.replace('\n', ' ')
        second_list.append(text)
    #print(len(second_list))

    #remove non_alpha characters
    third_list = []
    sentence = ''
    for text in second_list:
        sentence = ''.join(char for char in text if not char.isdigit())
        third_list.append(sentence)

    dataframe['pre_process_text'] = third_list

    # Commen/utilise as decided, removes all punctuation.
    # fourth_list = []
    # sentence_2 = ''
    # for text_2 in third_list:
    #     sentence_2 = ''.join(char for char in text_2 if char.isalpha())
    #     fourth_list.append(sentence_2)

    dataframe['pre_process_text'] = third_list

    #drop duplicates based purely on the pre processed text column
    dataframe.drop_duplicates(subset=['pre_process_text'], inplace=True)

    # final output
    return dataframe

def fix_text_characters_with_punctuation(dataframe):
    import pandas as pd
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
    punc = '''()-[]{};:'"\,<>./@#$%^&*_~'''
    for text in dataframe['pre_process_text']:
        for special in punc:
            text = text.replace(special, ' ')
        text = text.replace('\n', ' ')
        second_list.append(text)
    #print(len(second_list))

    #remove non_alpha characters
    third_list = []
    sentence = ''
    for text in second_list:
        sentence = ''.join(char for char in text if not char.isdigit())
        third_list.append(sentence)

    dataframe['pre_process_text'] = third_list

    # Commen/utilise as decided, removes all punctuation.
    # fourth_list = []
    # sentence_2 = ''
    # for text_2 in third_list:
    #     sentence_2 = ''.join(char for char in text_2 if char.isalpha())
    #     fourth_list.append(sentence_2)

    dataframe['pre_process_text'] = third_list

    #drop duplicates based purely on the pre processed text column
    dataframe.drop_duplicates(subset=['pre_process_text'], inplace=True)

    # final output
    return dataframe

def drop_irrelevant_topics(df):

    topics_to_drop=[
        '/sport/', '/sports/' '/culture/', '/lifestyle/', '/entertainment/',
        'sudoku', 'puzzle', 'crossword', 'style', '/female/',
        'parents', '/family/', 'travel', '/holiday/',
        'tvshowbiz','culture', 'magazine',
        'health','music','/arts/','recipes','/living/',
        '/food/','/shop/', '/best-buys/','/wellness/','/movie/','/series/','/shows/']
    # EDA: worths looking at how 'entertainment/tv/series' genre is so fckn predominant in right-winged publisher

    df = df[~df['link'].str.contains('|'.join(topics_to_drop), case=False, na=False)]

    return df.reset_index(drop=True)


if __name__ == "__main__":
    print(fix_text_characters(get_data_left()))
