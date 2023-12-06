import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

# from matplotlib import font_manager
# print(font_manager.findSystemFonts(fontpaths=None, fontext="ttf"))
# print(font_manager.findfont("American Typewriter"))


from keyword_search import search_keyword

def word_cloud_pipe(df1,df2,df3,df4,df5):
    x = get_words(df1,df2,df3,df4,df5)
    y = wordcloud(x)
    return None

def type_list(df):
    df["keyword_key_words"] = list(df["key"])
    return df

def get_words(df1,df2,df3,df4,df5):
    # ic(df1)
    # ic(df2)
    big_df = pd.concat([df1,df2,df3,df4,df5],axis=0).reset_index()

    big_df = type_list(big_df)

    empty_list = []

    for row in list(big_df["keyword_key_words"]):
        for elem in row:
            empty_list.append(elem)

    x = ' '.join(empty_list)

    return x

def wordcloud(x):
    ### import mask
    mask = np.array(Image.open('raw_data/news_mask.png'))

    ### instantiate word cloud
    wordcloud = WordCloud(mask = mask, max_font_size=500, max_words=55, background_color="white", font_path = 'raw_data/fonts/tower_of_silence/towerofsilenceexpand.ttf',
                      collocations=True,colormap = 'coolwarm', contour_width=2.0, contour_color='black').generate(x) #mode="RGBA", colormap = 'Reds', background_color="rgba(255, 255, 255, 0)"

    ### show figure
    plt.figure(figsize = (10,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off") # plt.figsize(10,6)
    plt.show()

    return None


if __name__ == "__main__":
    print(word_cloud_pipe(*(search_keyword('covid'))))
