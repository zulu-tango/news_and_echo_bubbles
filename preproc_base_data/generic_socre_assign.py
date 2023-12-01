import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

from preproc_base_data.pre_proc_pipe import concat_for_pre_built

"""
    dict based on scoring system: -2, -1, 0, 1, 2
    -2 = strong left, -1 = left, 1 = right, 2 = strong right, 0 = centre
"""
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
 'www.apnews.com': -1,
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
 'www.oann.com': 2}


"""
    dict based on scoring system: 0, 0.5, 1
    0 = left, 1 = right, 0.5 = centre
"""

dict_binary = {'www.alternet.org': 0.0,
 'www.theatlantic.com': 0.0,
 'www.democracynow.org': 0.0,
 'www.thedailybeast.com': 0.0,
 'www.huffpost.com': 0.0,
 'www.theintercept.com': 0.0,
 'www.jacobinmag.com': 0.0,
 'www.motherjones.com': 0.0,
 'www.msnbc.com': 0.0,
 'www.newyorker.com': 0.0,
 'www.nytimes.com': 0.0,
 'www.thenation.com': 0.0,
 'www.slate.com': 0.0,
 'www.vox.com': 0.0,
 'www.abcnews.go.com': 0.0,
 'www.apnews.com': 0.0,
 'www.axios.com': 0.0,
 'www.bloomberg.com': 0.0,
 'www.cbsnews.com': 0.0,
 'www.cnn.com': 0.0,
 'www.theguardian.com': 0.0,
 'www.insider.com': 0.0,
 'www.nbcnews.com': 0.0,
 'www.npr.org': 0.0,
 'www.politico.com': 0.0,
 'www.propublica.org': 0.0,
 'www.time.com': 0.0,
 'www.washingtonpost.com': 0.0,
 'www.usatoday.com': 0.0,
 'www.yahoo.com': 0.0,
 'www.bbc.com': 0.5,
 'www.csmonitor.com': 0.5,
 'www.forbes.com': 0.5,
 'www.marketwatch.com': 0.5,
 'www.newsnationnow.com': 0.5,
 'www.newsweek.com': 0.5,
 'www.reuters.com': 0.5,
 'www.realclearpolitics.com': 0.5,
 'www.thehill.com': 0.5,
 'www.wsj.com': 1.0,
 'www.thedispatch.com': 1.0,
 'www.theepochtimes.com': 1.0,
 'www.foxbusiness.com': 1.0,
 'www.nationalreview.com': 1.0,
 'www.nypost.com': 1.0,
 'www.reason.com': 1.0,
 'www.washingtonexaminer.com': 1.0,
 'www.washingtontimes.com': 1.0,
 'www.theamericanconservative.com': 1.0,
 'www.spectator.org': 1.0,
 'www.breitbart.com': 1.0,
 'www.theblaze.com': 1.0,
 'www.cbn.com': 1.0,
 'www.dailycaller.com': 1.0,
 'www.dailymail.co.uk': 1.0,
 'www.dailywire.com': 1.0,
 'www.thepostmillennial.com': 1.0,
 'www.foxnews.com': 1.0,
 'www.thefederalist.com': 1.0,
 'www.ijr.com': 1.0,
 'www.newsmax.com': 1.0,
 'www.freebeacon.com': 1.0,
 'www.oann.com': 1.0}


"""
    This function must be called post the basic cleaning function, it requires the abse URL added in manual pre proc function.
"""
def assign_score_5_scores(df):
    # print(df['urls'])
    df["5_step_classifier"] = df['urls'].map(scoring_dict)
    return df

def assign_score_0_half_1(df):
    # print(df['urls'])
    df["3_step_classifier"] = df['urls'].map(scoring_dict)
    return df

def one_hot_encoder_3(df):
    encoder = OneHotEncoder()#categories=["strong_left", "left", "centre", "right", "strong_right"])
    encoded_result = encoder.fit_transform(df[["3_step_classifier"]])
    names = encoder.get_feature_names_out()
    df_result = pd.DataFrame(encoded_result)
    return df_result


if __name__ == "__main__":
    print((assign_score_0_half_1(concat_for_pre_built())))
    # print(assign_score_0_half_1(concat_for_pre_built()).info())
