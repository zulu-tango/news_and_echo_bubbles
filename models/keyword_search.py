import os
import pandas as pd
import ast


path = os.getcwd()

def search_keyword(topic):
    #search from raw data post-embedding and training
    #find way to search from sql for streamlit demo
    df_ll, df_l, df_c, df_r, df_rr = biases()

    keyword = topic
    returned_articles = []
    for index, row in enumerate(df_ll.keywords):
        if keyword in row:
            returned_articles.append((df_ll['title'][index],df_ll['pred_class'][index],df_ll['link'][index],df_ll.keywords[index][keyword]))
    output_df_ll = pd.DataFrame(returned_articles,columns=['title','bias','link','keyword_score'])
    output_df_ll = output_df_ll.sort_values(by=['keyword_score'],ascending=False)

    returned_articles = []
    for index, row in enumerate(df_l.keywords):
        if keyword in row:
            returned_articles.append((df_l['title'][index],df_l['pred_class'][index],df_l['link'][index],df_l.keywords[index][keyword]))
    output_df_l = pd.DataFrame(returned_articles,columns=['title','bias','link','keyword_score'])
    output_df_l = output_df_l.sort_values(by=['keyword_score'],ascending=False)

    returned_articles = []
    for index, row in enumerate(df_c.keywords):
        if keyword in row:
            returned_articles.append((df_c['title'][index],df_c['pred_class'][index],df_c['link'][index],df_c.keywords[index][keyword]))
    output_df_c = pd.DataFrame(returned_articles,columns=['title','bias','link','keyword_score'])
    output_df_c = output_df_c.sort_values(by=['keyword_score'],ascending=False)

    returned_articles = []
    for index, row in enumerate(df_r.keywords):
        if keyword in row:
            returned_articles.append((df_r['title'][index],df_r['pred_class'][index],df_r['link'][index],df_r.keywords[index][keyword]))
    output_df_r = pd.DataFrame(returned_articles,columns=['title','bias','link','keyword_score'])
    output_df_r = output_df_r.sort_values(by=['keyword_score'],ascending=False)

    returned_articles = []
    for index, row in enumerate(df_rr.keywords):
        if keyword in row:
            returned_articles.append((df_rr['title'][index],df_rr['pred_class'][index],df_rr['link'][index],df_rr.keywords[index][keyword]))
    output_df_rr = pd.DataFrame(returned_articles,columns=['title','bias','link','keyword_score'])
    output_df_rr = output_df_rr.sort_values(by=['keyword_score'],ascending=False)

    return output_df_ll[:2], output_df_l[:2], output_df_c[:2], output_df_r[:2], output_df_rr[:2]

def biases():
    df = pd.read_csv(f'{path}/raw_data/base_table_2023-12-04.csv')
    for index, row in enumerate(df.keywords):
        df.keywords[index] = ast.literal_eval(df.keywords[index])

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
