import os
import pandas as pd
import ast
from datetime import date
from collections import Counter
path = os.getcwd()

def cached_data():
    data= pd.read_csv(f'{path}/raw_data/base_table_2023-12-05_updated.csv')
    for index, row in enumerate(data.keywords):
        data.keywords[index] = ast.literal_eval(data.keywords[index])
    return data

def trending_topics():
    df = cached_data()

    list_of_keywords = []
    trending_topics = []
    mask = df['pdate'] == df['pdate'].max()
    df = df[mask]
    df.reset_index(drop=True,inplace=True)
    for i in range(len(df.keywords)):
        for key in df.keywords[i].keys():
            list_of_keywords.append((key,))

    temp = set()
    counter = Counter(list_of_keywords)
    for word in list_of_keywords:
        if word not in temp:
            trending_topics.append((counter[word], ) + word)
            temp.add(word)


    trending = pd.DataFrame(trending_topics,columns=['count','word'])

    trending.sort_values(by='count',ascending=False,inplace=True)
    trending.reset_index(drop=True,inplace=True)

    topic_1 = trending.word[0]
    topic_2 = trending.word[1]
    topic_3 = trending.word[2]
    topic_4 = trending.word[3]
    topic_5 = trending.word[4]

    return topic_1, topic_2, topic_3, topic_4, topic_5

def search_keyword(topic):
    #search from raw data post-embedding and training
    #find way to search from sql for streamlit demo
    df_ll, df_l, df_c, df_r, df_rr = biases()

    keyword = topic
    returned_articles = []
    for index, row in enumerate(df_ll.keywords):
        if keyword in row:
            returned_articles.append((df_ll['link'][index],df_ll['pdate'][index],df_ll['title'][index],df_ll['author'][index],df_ll['text'][index],df_ll['urls'][index],df_ll['pred_class'][index],df_ll.keywords[index].keys(),df_ll.keywords[index][keyword])) ##TODO get key names out into dataframe
    output_df_ll = pd.DataFrame(returned_articles,columns=['link','pdate','title','author','text','urls','pred_class','key','keyword_score'])
    output_df_ll = output_df_ll.sort_values(by=['keyword_score'],ascending=False)
    output_df_ll.reset_index(drop=True,inplace=True)

    returned_articles = []
    for index, row in enumerate(df_l.keywords):
        if keyword in row:
            returned_articles.append((df_l['link'][index],df_l['pdate'][index],df_l['title'][index],df_l['author'][index],df_l['text'][index],df_l['urls'][index],df_l['pred_class'][index],df_l.keywords[index].keys(),df_l.keywords[index][keyword]))
    output_df_l = pd.DataFrame(returned_articles,columns=['link','pdate','title','author','text','urls','pred_class','key','keyword_score'])
    output_df_l = output_df_l.sort_values(by=['keyword_score'],ascending=False)
    output_df_l.reset_index(drop=True,inplace=True)

    returned_articles = []
    for index, row in enumerate(df_c.keywords):
        if keyword in row:
            returned_articles.append((df_c['link'][index],df_c['pdate'][index],df_c['title'][index],df_c['author'][index],df_c['text'][index],df_c['urls'][index],df_c['pred_class'][index],df_c.keywords[index].keys(),df_c.keywords[index][keyword]))
    output_df_c = pd.DataFrame(returned_articles,columns=['link','pdate','title','author','text','urls','pred_class','key','keyword_score'])
    output_df_c = output_df_c.sort_values(by=['keyword_score'],ascending=False)
    output_df_c.reset_index(drop=True,inplace=True)

    returned_articles = []
    for index, row in enumerate(df_r.keywords):
        if keyword in row:
            returned_articles.append((df_r['link'][index],df_r['pdate'][index],df_r['title'][index],df_r['author'][index],df_r['text'][index],df_r['urls'][index],df_r['pred_class'][index],df_r.keywords[index].keys(),df_r.keywords[index][keyword]))
    output_df_r = pd.DataFrame(returned_articles,columns=['link','pdate','title','author','text','urls','pred_class','key','keyword_score'])
    output_df_r = output_df_r.sort_values(by=['keyword_score'],ascending=False)
    output_df_r.reset_index(drop=True,inplace=True)

    returned_articles = []
    for index, row in enumerate(df_rr.keywords):
        if keyword in row:
            returned_articles.append((df_rr['link'][index],df_rr['pdate'][index],df_rr['title'][index],df_rr['author'][index],df_rr['text'][index],df_rr['urls'][index],df_rr['pred_class'][index],df_rr.keywords[index].keys(),df_rr.keywords[index][keyword]))
    output_df_rr = pd.DataFrame(returned_articles,columns=['link','pdate','title','author','text','urls','pred_class','key','keyword_score'])
    output_df_rr = output_df_rr.sort_values(by=['keyword_score'],ascending=False)
    output_df_rr.reset_index(drop=True,inplace=True)

    return output_df_ll, output_df_l, output_df_c, output_df_r, output_df_rr

def biases():
    df = cached_data()

    mask_ll = df['pred_class'] =='left'
    mask_l = df['pred_class'] =='leans left'
    mask_c = df['pred_class'] =='centre'
    mask_r = df['pred_class'] =='leans right'
    mask_rr = df['pred_class'] =='right'
    df_ll = df[mask_ll]
    df_ll.reset_index(drop=True,inplace=True)
    df_l = df[mask_l]
    df_l.reset_index(drop=True,inplace=True)
    df_c = df[mask_c]
    df_c.reset_index(drop=True,inplace=True)
    df_r = df[mask_r]
    df_r.reset_index(drop=True,inplace=True)
    df_rr = df[mask_rr]
    df_rr.reset_index(drop=True,inplace=True)

    return df_ll, df_l, df_c, df_r, df_rr

if __name__ == "__main__":
    print(search_keyword('biden'))
