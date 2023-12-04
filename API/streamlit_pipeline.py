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

def clickable_cells(row):
    # Create a button for each cell in the row
    for col, value in row.iteritems():
        button_label = f"Click {value} in {col}"
        if st.button(button_label):
            # Handle the button click here (e.g., display more information)
            st.write(f"You clicked {value} in {col}")

def color_cells_row_wise(row):
    # Define a function to apply color to cells based on values in the row
    colors = ['background-color: #004687' if val == 'left' else 'background-color: #89CFF0' if val == 'leans left' else 'background-color: #AA0000' if val == 'right' else 'background-color: #E67150' if val == 'leans right' else 'background-color: black' for val in row]
    return colors

def main():
    st.set_page_config(page_title="News and Biases",layout="wide")
    #pd.set_option('display.max_colwidth', None)

    # Add a logo/picture to the app
    logo = "/home/zoetustain/code/zulu-tango/news_and_echo_bubbles/News_logo.png"  # Replace with the actual path to your logo
    st.image(logo, width=200)  # Adjust width as needed

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


        df_left = pd.concat([df_ll,df_l],ignore_index=True)
        df_right = pd.concat([df_rr,df_r],ignore_index=True)

        styled_df_left = df_left.style.apply(color_cells_row_wise, axis=1)
        styled_df_centre = df_c.style.apply(color_cells_row_wise, axis=1)
        styled_df_right = df_right.style.apply(color_cells_row_wise, axis=1)

        # for i in range(2):
        #     df_ll_styled = df_left.style.applymap(color_cells(df_ll.bias[i]))


        col1, col2, col3 = st.columns(3)
        col1.dataframe(styled_df_left)
        col2.dataframe(styled_df_centre)
        col3.dataframe(styled_df_right)

        progress_bar.empty()


    # Add a placeholder for dynamic content
    placeholder = st.empty()

    # Add a click functionality
    if st.button("Select and article for more information"):
        st.table(df_ll)
        # Show extra information when the button is clicked
        placeholder.text("Extra Information: This is additional information revealed when you click the button.")



if __name__ == "__main__":
    main()
