import pandas as pd
import os

path = os.getcwd()
from datetime import date

date = date.today()

from google.cloud.vision import *
# from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/barnabykempster/code/Barnaby323/gcp/wagon-bootcamp-66653-4434b235047c.json'

GCP_PROJECT = 'news-and-echo-bubbles'
# BQ_DATASET = 'preproc_base_table_2023_12_06.csv'

from google.cloud import bigquery

@st.cache_data
def get_master_df():
    '''function that returns the full master district df.
    Dataframe contains district name (primary key), lat_lons for the center,
    lat_lons for the edges of rectangle around area, and the area of the
    rectangle in Hectares'''

    client = bigquery.Client(project='news-and-echo-bubbles')

    query = f"""
            SELECT *
            FROM {GCP_PROJECT}.preproc_scraped_news.scraped_news_preprocessed_2023_12_06
            ORDER BY HECTARES DESC
        """

    client = bigquery.Client(project=GCP_PROJECT)
    query_job = client.query(query)
    result = query_job.result()
    df = result.to_dataframe()
    return df

    # sql = """
    #     SELECT *
    #     FROM 'base_table_2023-12-06.csv'
    # """
    # pandas_gbq.context.credentials = credentials
    # pandas_gbq.context.project = "your-project-id"


    # x = pandas_gbq.read_gbq(sql, project_id=project_id)
    # df = pd.DataFrame(x)
    # # df = pd.DataFrame(results)
    # return df

def get_data():
    data = pd.read_csv(f"{path}/raw_data/friday_data.csv")
    data_2 = pd.read_csv(f'{path}/raw_data/scraped_saturday.csv')
    data_3 = pd.read_csv(f'{path}/raw_data/scraped_data_combined_sunday.csv')
    combined_df = pd.concat([data,data_2,data_3])
    combined_df.to_csv(f'{path}/raw_data/combined_data_{date}.csv')
    return combined_df

def get_data_right():
    brainded_right = pd.read_csv(f"{path}/raw_data/braindedright.csv")
    return brainded_right

def get_data_left():
    brainded_left = pd.read_csv(f"{path}/raw_data/braindedleft.csv")
    return brainded_left

def get_data_generic(csv_name="braindedright"):
    data = pd.read_csv(f"{path}/raw_data/{csv_name}.csv")
    return data

def text_for_pre_built_pre_proc(dataframe):
    df_1 = dataframe[['text','classifier']].astype('str')
    # df_1 = dataframe[['text']]
    return df_1


if __name__ == "__main__":
    # print(get_data_left())
    # print(date.today())
    # print(get_data())
    print(get_master_df())
