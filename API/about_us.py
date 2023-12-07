import streamlit as st
import os

########################## about us page  #####################


def page_profile():

    # set CSS style to round all images expect the one with the "exclude-me" tag (i.e. linkedin icons)
    st.markdown("""
    <style>
        img:not(#exclude-me) {border-radius: 50%}
    </style>

    """, unsafe_allow_html=True)

    ############################### Barnaby info #######################################
    # create two cols, one for profile photo and the other with the social networks links
    col1, mid, col2 = st.columns([1,2,20],gap="medium")

    with col1:
        st.image(os.path.abspath('Images/Barnaby.png'), width=105) #path of the picture

    with col2:
        st.markdown("**Barnaby Kempster**")
        st.write("""
    <img src="https://github.githubassets.com/favicons/favicon.svg" width="20" border-radius="50"> **Github profile**: https://github.com/Barnaby323

    <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/barnaby-kempster/
                """, unsafe_allow_html=True)
    # add large blank space
    st.write("#")
    ############################### Connor Gower info #######################################
    # create two cols, one for profile photo and the other with the social networks links
    col1, mid, col2 = st.columns([1,2,20],gap="medium")
    with col1:
        st.image(os.path.abspath('Images/Connor.png'), width=105)#path of the picture

    with col2:
        st.markdown("**Connor Gower**")
        st.markdown("""
    <img class="image backArrow" src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/connorgower

    <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/connor-gower/


                """, unsafe_allow_html=True)

    # add large blank space
    st.write("#")
    ############################### Manuel Puente info #######################################
    # create two cols, one for profile photo and the other with the social networks links

    col1, mid, col2 = st.columns([1,2,20],gap="medium")

    with col1:
        st.image(os.path.abspath('Images/Manuel.png'), width=105)#path of the picture

    with col2:
        st.markdown("**Manuel Puente**")
        st.write("""
    <img src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/Manu2023ds

    <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/manuel-p-29223629/

                """, unsafe_allow_html=True)

    # add large blank space
    st.write("#")
    ############################### Zoe Tustain info #######################################
    # create two cols, one for profile photo and the other with the social networks links

    col1, mid, col2 = st.columns([1,2,20],gap="medium")

    with col1:
        st.image(os.path.abspath('Images/Zoe.png'), width=105)#path of the picture

    with col2:
        st.markdown("**Zoe Tustain**")
        st.write("""
    <img src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/zulu-tango

    <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/zoetustain/

                """, unsafe_allow_html=True)

    # add large blank space
    st.write("#")
    ############################### COMLAN Renato info #######################################
    # create two cols, one for profile photo and the other with the social networks links
    col1, mid, col2 = st.columns([1,2,20],gap="medium")

    with col1:
        st.image(os.path.abspath('Images/Renato.png'), width=105)#path of the picture

    with col2:
        st.markdown("**Renato COMLAN**")
        st.write("""
    <img src="https://github.githubassets.com/favicons/favicon.svg" width="20"> **Github profile**: https://github.com/cmlnrnt

    <img id='exclude-me' src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="20"> **LinkedIn**: https://www.linkedin.com/in/renato-comlan/

                """, unsafe_allow_html=True)
