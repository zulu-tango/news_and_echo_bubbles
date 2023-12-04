import pandas as pd
import numpy as np
from preproc_base_data.manual_pre_proc import manual_pre_process,manual_pre_process_2, base_author_col_add, fix_text_characters, fix_text_characters_with_punctuation
from preproc_base_data.score import right_data_add_0, left_data_add_0
from preproc_base_data.data import get_data_left, get_data_right, get_data
from preproc_base_data.data import text_for_pre_built_pre_proc
#Combined preproc function

def data_pre_proc():
    scoring_dict = {'www.alternet.org': -2,
                            'www.theatlantic.com': -2,
                            'www.democracynow.org': -2,
                            'www.thedailybeast.com': -2,
                            'www.huffpost.com': -2,
                            'www.theintercept.com': -2,
                            'www.jacobinmag.com': -2,
                            'www.motherjones.com': -2,
                            'www.msnbc.com': -2,
                            'www.newyorker.com': -2,
                            'www.nytimes.com': -1,
                            'www.thenation.com': -2,
                            'www.slate.com': -2,
                            'www.vox.com': -2,
                            'www.abcnews.go.com': -1,
                            'apnews.com': -1,
                            'www.axios.com': -1,
                            'www.bloomberg.com': -1,
                            'www.cbsnews.com': -1,
                            'www.cnn.com': -1,
                            'www.theguardian.com': -1,
                            'www.insider.com': -1,
                            'www.nbcnews.com': -1,
                            'www.npr.org': -1,
                            'www.politico.com': -1,
                            'www.propublica.org': -1,
                            'www.time.com': -1,
                            'www.washingtonpost.com': -1,
                            'www.usatoday.com': -1,
                            'www.yahoo.com': -1,
                            'www.bbc.com': 0,
                            'www.csmonitor.com': 0,
                            'www.forbes.com': 0,
                            'www.marketwatch.com': 0,
                            'www.newsnationnow.com': 0,
                            'www.newsweek.com': 0,
                            'www.reuters.com': 0,
                            'www.realclearpolitics.com': 0,
                            'www.thehill.com': 0,
                            'www.wsj.com': 1,
                            'www.thedispatch.com': 1,
                            'www.theepochtimes.com': 1,
                            'www.foxbusiness.com': 1,
                            'www.nationalreview.com': 2,
                            'www.nypost.com': 2,
                            'www.reason.com': 1,
                            'www.washingtonexaminer.com': 1,
                            'www.washingtontimes.com': 1,
                            'www.theamericanconservative.com': 2,
                            'www.spectator.org': 2,
                            'www.breitbart.com': 2,
                            'www.theblaze.com': 2,
                            'www.cbn.com': 2,
                            'www.dailycaller.com': 2,
                            'www.dailymail.co.uk': 2,
                            'www.dailywire.com': 2,
                            'www.thepostmillennial.com': 2,
                            'www.foxnews.com': 2,
                            'www.thefederalist.com': 2,
                            'www.ijr.com': 2,
                            'www.newsmax.com': 2,
                            'www.freebeacon.com': 2,
                            'www.oann.com': 2,'thedailybeast.freshdesk.com':-2,
                   'theathletic.com': -2,
                   'cooking.nytimes.com':-1,
                   'cn.nytimes.com':-1,
                   'www.hulu.com':-1,
                   'www.bloomberg.co.jp':-1,
                   'bloomberg.com':-1,
                   'tunein.com':-1,
                   'www.paramountplus.com':-1,
                   'projects.propublica.org':-1,
                   'features.propublica.org':-1,
                   'time.com':-1,
                   'cm.usatoday.com':-1,
                   'reviewed.usatoday.com':-1,
                   'puzzles.usatoday.com':-1,
                   'finance.yahoo.com':-1,
                   'sports.yahoo.com':-1,
                   'news.yahoo.com':-1,
                   'autos.yahoo.com':-1,
                   'sg.yahoo.com':-1,
                   'sg.news.yahoo.com':-1,
                   'sg.finance.yahoo.com':-1,
                   'sg.style.yahoo.com':-1,
                   'tw.news.yahoo.com':-1,
                   'tw.sports.yahoo.com':-1,
                   'travel.yahoo.com.tw':-1,
                   'autos.yahoo.com.tw':-1,
                   'style.yahoo.com.tw':-1,
                   'www.edh.tw':-1,
                   'tw.tv.yahoo.com':-1,
                   'tw.promo.yahoo.com':-1,
                   'movies.yahoo.com.tw':-1,
                   'uk.yahoo.com':-1,
                   'uk.news.yahoo.com':-1,
                   'uk.style.yahoo.com':-1,
                   'uk.finance.yahoo.com':-1,
                   'uk.sports.yahoo.com':-1,
                   'qc.yahoo.com':-1,
                   'fr.style.yahoo.com':-1,
                   'fr.news.yahoo.com':-1,
                   'ca.sports.yahoo.com':-1,
                   'espanol.yahoo.com':-1,
                   'es-us.noticias.yahoo.com':-1,
                   'es-us.finanzas.yahoo.com':-1,
                   'es-us.vida-estilo.yahoo.com':-1,
                   'hk.news.yahoo.com':-1,
                   'hk.finance.yahoo.com':-1,
                   'ca.yahoo.com':-1,
                   'ca.news.yahoo.com':-1,
                   'ca.finance.yahoo.com':-1,
                   'ca.style.yahoo.com':-1,
                   'malaysia.yahoo.com':-1,
                   'malaysia.news.yahoo.com':-1,
                   'www.the-independent.com':-1,
                   'au.yahoo.com':-1,
                   'au.lifestyle.yahoo.com':-1,
                   'au.news.yahoo.com':-1,
                   'au.sports.yahoo.com':-1,
                   'au.finance.yahoo.com':-1,
                   'de.yahoo.com':-1,
                   'de.nachrichten.yahoo.com':-1,
                   'de.style.yahoo.com':-1,
                   'de.finance.yahoo.com':-1,
                   'www.artnews.com':-1,
                   'nypost.com':1,
                   'captimes.com':-1,
                   'reuters.com':-0,
                   'wsj.com':-0,
                   'staging.theepochtimes.com':1,
                   'theepochtimes.gr':1,
                   'es.theepochtimes.com':1,
                   'help.theepochtimes.au':1,
                   'pagesix.com':1,
                   'decider.com':1,
                   'reason.com':1,
                   'www.thefire.org':1,
                   'law.justia.com':1,
                   'www.inquirer.com':1,
                   'www.thedp.com':1,
                   'ndlawreview.org':1,
                   'www.lawfaremedia.org':1,
                   'www.ca5.uscourts.gov':1,
                   'pacificlegal.org':1,
                   'thehill.com':1,
                   'volokh.com':1,
                   'marketurbanism.com':1,
                   'web.archive.org':1,
                   'johnhcochrane.blogspot.com':1,
                   'tushnet.blogspot.com':1,
                   'www.scotusblog.com':1,
                   'www.yalejreg.com':1,
                   'www.oyez.org':1,
                   'reason.plannedgiving.org':1,
                   'reason.org':1}
    data = get_data()
    df_1 = manual_pre_process_2(dataframe=data)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters_with_punctuation(dataframe=df_2)
    df_3.drop(columns=['Unnamed: 0','Unnamed: 0.1'],inplace=True)
    df_3["5_step_classifier"] = df_3['urls'].map(scoring_dict)
    return df_3


def left_pipe_pre_proc():
    data = get_data_left()
    df_0 = left_data_add_0(dataframe=data)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

def right_pipe_pre_proc():
    data = get_data_right()
    df_0 = right_data_add_0(dataframe=data)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters(dataframe=df_2)
    return df_3

#Joining dataframes

def join_dataframes(dataframe_1, dataframe_2):
    df_concat = dataframe_1.merge(dataframe_2,how='outer')
    # df_concat =df_concat.reset_index(drop=True)
    return df_concat

#Combined pipe to be ready for pre built online transformers
def pipe_for_pre_made_transformer_left():
    data = get_data_left()
    df_1 = left_data_add_0(dataframe=data)
    df_2 = text_for_pre_built_pre_proc(dataframe=df_1)
    return df_2

def pipe_for_pre_made_transformer_right():
    data = get_data_right()
    df_1 = right_data_add_0(dataframe=data)
    df_2 = text_for_pre_built_pre_proc(dataframe=df_1)
    return df_2

#combined pipe for left and right, returns fully cleaned data.

def concat_for_pre_built():
    df_left = left_pipe_pre_proc()
    df_right = right_pipe_pre_proc()
    combined_df = join_dataframes(dataframe_1=df_left,dataframe_2=df_right)
    return combined_df.drop(columns = ['level_0', 'index', 'Unnamed: 0'])

"""
    From here on the functions are the same as above but use the function from manual_pre_proc that maintains
    ! and ? in the text, on the premise that they add context in certain situations.
"""
#combined pre proc with the ? and ! maintained

def left_pipe_pre_proc_with_punc():
    data = get_data_left()
    df_0 = left_data_add_0(dataframe=data)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters_with_punctuation(dataframe=df_2)
    return df_3

def right_pipe_pre_proc_with_punc():
    data = get_data_right()
    df_0 = right_data_add_0(dataframe=data)
    df_1 = manual_pre_process(dataframe=df_0)
    df_2 = base_author_col_add(dataframe=df_1)
    df_3 = fix_text_characters_with_punctuation(dataframe=df_2)
    return df_3

#full pipe utilising the two functions below

def concat_for_pre_built_with_punc():
    df_left = left_pipe_pre_proc_with_punc()
    df_right = right_pipe_pre_proc_with_punc()
    combined_df = join_dataframes(dataframe_1=df_left,dataframe_2=df_right)
    return combined_df.drop(columns = ['level_0', 'index', 'Unnamed: 0'])

if __name__ == "__main__":
    print(data_pre_proc())
    #print(concat_for_pre_built_with_punc()['pre_process_text'][2600])

#if __name__ == "__main__":
    #print(concat_for_pre_built())
