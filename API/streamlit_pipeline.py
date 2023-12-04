import streamlit as st
import pandas as pd  # Import the Pandas library
from models.keyword_search import search_keyword
import time


def trending_topics():
    # TODO: code trending topics function
    return tt_1, tt_2, tt_3

def search(query):
    # Perform a search operation (replace this with your own search logic)

    # For demonstration, creating three different DataFrames with different columns

    df_ll, df_l, df_c, df_r, df_rr = search_keyword(query)
    df_ll.style.hide(axis="index")
    return df_ll[['bias','title','link']],df_l[['bias','title','link']],df_c[['bias','title','link']],df_r[['bias','title','link']],df_rr[['bias','title','link']]

def main():
    st.set_page_config(layout="wide")
    pd.set_option('display.max_colwidth', None)
    st.title("News and Biases")

    # Add a search box for selecting a topic
    topic = st.text_input("Choose a topic: ")

    # Add a search button
    if st.button("Search"):
        #st.markdown("<h4 style='color: green; font-size: 10px;'>Searching articles... Please wait.</h4>", unsafe_allow_html=True)
        progress_bar = st.progress(0, text='searching articles... please wait')

        # Perform the search when the button is clicked
        df_ll, df_l, df_c, df_r, df_rr = search(topic)

        for percent_complete in range(100):
                time.sleep(0.02)
                progress_bar.progress(percent_complete + 1)

        col1, col2, col3 = st.columns(3)
        col1.dataframe(pd.concat([df_ll,df_l],ignore_index=True))
        col2.dataframe(df_c)
        col3.dataframe(pd.concat([df_rr,df_r],ignore_index=True))

        progress_bar.empty()

    st.table(df_ll)

    # Add a placeholder for dynamic content
    placeholder = st.empty()

    # Add a click functionality
    if st.button("Select and article for more information"):
        st.table(df_ll)
        # Show extra information when the button is clicked
        placeholder.text("Extra Information: This is additional information revealed when you click the button.")



if __name__ == "__main__":
    main()
