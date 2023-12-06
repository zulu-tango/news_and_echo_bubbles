import streamlit as st
import pandas as pd  # Import the Pandas library
from models.keyword_search import search_keyword, trending_topics
import time
from datetime import date, timedelta


def trending():
    # TODO: code trending topics function
    topic_1, topic_2, topic_3, topic_4, topic_5 = trending_topics()
    return topic_1, topic_2, topic_3, topic_4, topic_5

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
    colors = ['background-color: #004687' if val == 'left' else 'background-color: #6699CC' if val == 'leans left' else 'background-color: #AA0000' if val == 'right' else 'background-color: #E67150' if val == 'leans right' else 'background-color: white' for val in row]
    return colors



def main():
    st.set_page_config(page_title="News and Biases",layout="wide")
    #pd.set_option('display.max_colwidth', None)

    container = st.container()
    logo_col, header_col = container.columns(2)

    # Add a logo
    with logo_col:
        logo = st.image("/home/zoetustain/code/zulu-tango/news_and_echo_bubbles/News_logo.png", width=250)

    # Boxed header
    with header_col:
        news_all, news_uk, news_us = st.columns(3)
        # five buttons on the same row

        if news_all.button('', key='logo_button', help='Click to go to the logo URL'):
            st.write('You selected all news sources')
            # Add the action you want when the logo is clicked

        # Logo image
        st.image("/home/zoetustain/code/zulu-tango/news_and_echo_bubbles/images/world_flag.png", width=50)

        # world = st.image("/home/zoetustain/code/zulu-tango/news_and_echo_bubbles/images/world_flag.png", width=50)
        # image_world = st.image('/home/zoetustain/code/zulu-tango/news_and_echo_bubbles/images/world_flag.png', width=100)
        # button_world = world.button('world',key='button_world')
        button_uk = news_uk.button('UK')
        button_us = news_us.button('US')

        st.markdown(
            """
            <div style="text-align: center; border:1px solid #d3d3d3; padding: 10px; border-radius: 10px; background-color: #f5f5f5;">
                <h1 style="color: #333;font-size: 20px;">TRENDING TOPICS</h1>
            </div>
            """,
            unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        topic_1, topic_2, topic_3, topic_4, topic_5 = trending()
        tt_1, tt_2, tt_3, tt_4, tt_5 = st.columns(5)
        # five buttons on the same row
        button_topic_1 = tt_1.button(topic_1)
        button_topic_2 = tt_2.button(topic_2)
        button_topic_3 = tt_3.button(topic_3)
        button_topic_4 = tt_4.button(topic_4)
        button_topic_5 = tt_5.button(topic_5)




    topic = st.text_input("ENTER A SEARCH TOPIC: ", '')
    #date_options = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03'])

    #selected_option = st.slider("Select an date range", options=pd.DataFrame[1, 2, 3, 4, 5])
    # start_time = st.slider(
    #     "When do you start?",
    #     value=date.today(),
    #     format="DD/MM/YY")
    # st.write("Start time:", start_time)

    date_range = st.slider("Date range:", min_value = date.today(), max_value= date.today()-timedelta(14), value=(date.today(), date.today()-timedelta(14)))

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


    # # Add a placeholder for dynamic content
    # placeholder = st.empty()

    # # Add a click functionality
    # if st.button("Select and article for more information"):
    #     st.table(df_ll)
    #     # Show extra information when the button is clicked
    #     placeholder.text("Extra Information: This is additional information revealed when you click the button.")



if __name__ == "__main__":
    main()
