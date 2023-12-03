import os
import pandas as pd
import ast


path = os.getcwd()

def search_keyword():
    #search from raw data post-embedding and training
    #find way to search from sql for streamlit demo
    df_ll, df_l, df_c, df_r, df_rr = biases()
    df_list = [df_ll, df_l, df_c, df_r, df_rr]

    keyword = input('searchword: ')
    for df in df_list:
        returned_articles = []
        for index, row in enumerate(df.keywords):
            if keyword in row:
                returned_articles.append((df['text'][index],df['urls'],df.keywords[index][keyword]))
        output_df = pd.DataFrame(returned_articles,columns=[f'text_{df.pred_class[0]}','urls','keyword_score'])
        output_df = output_df.sort_values(by=['keyword_score'],ascending=False)
        print(output_df[:2])
    return output_df

def biases():
    df = pd.read_csv(f'{path}/raw_data/predicted_sentiment.csv')
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
    print(search_keyword())
