import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity

from PIL import Image

st.set_page_config(page_title='P-Pop to the Top!', layout="wide")
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

def project():
    st.title('Catapulting Pinoy Pop to the Top')
    st.subheader('by Data Science Fellowship Cohort 7 - Group 1')
    st.write('Bym, Ben, Matt, Miggy, Nilly, Robby (mentored by Danilo)')

    intro_image = Image.open('./Sprint_2_G1_SB19FTW/Slide1.png')

    col1, col2 = st.beta_columns(2)
    with col1:
        st.image(intro_image)
    with col2:
        st.markdown(
            "We harnessed the power of data to decode the **TikTok** sound and inspire **SB19’s** new hit track designed to *top the charts*."
        )

     
def sb19():
    st.title('Introducing SB19')
    st.write("")
    st.subheader(
            "Meet Josh, Pablo, Stell, Ken, and Justin"
        )
    col1, col2 = st.beta_columns(2)
    with col1:
        sb19_pic = Image.open('./Sprint_2_G1_SB19FTW/Slide2.png')
        st.image(sb19_pic)
    with col2:
        st.markdown(
            " - One of the up and coming **Pinoy Pop (P-Pop)** groups"
        )
        st.markdown(
            " - Trained for 3 years by ShowBT Philippines"
        )
        st.markdown(
            " - Active since 2018"
        )
        st.markdown(
            " - The first Filipino and Southeast Asian act to be nominated in **Billboard Music Awards** for the *Top Social Artist* category"
        )
    st.subheader(
            "On Social Media:"
        )
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.subheader('**Facebook**')
        st.write("**1.4M Followers**")

    with col2:
        st.subheader('**Twitter**')
        st.write("**422k Followers**")

    with col3:
        st.subheader('**Instagram**')
        st.write("**454K Followers**")


def sb19_spotify():
    st.title('SB19 and Spotify: At A Glance')

    col1, col2 = st.beta_columns(2)
    with col1:
        sb19_follow = Image.open("./Sprint_2_G1_SB19FTW/Slide3.png")
        st.image(sb19_follow)
        st.markdown(
            "SB19 has a **massive following** on social media but **relatively low streams** on Spotify."
        )
    with col2:
        tiktok_follow = Image.open("./Sprint_2_G1_SB19FTW/Slide4.png")
        st.image(tiktok_follow)
        st.markdown(
            "These artists have **smaller followings** but **higher streams.**"
        )
        st.write("")
        with st.beta_expander("What do they have in common?"):
            
            tiktok_logo = Image.open("img/tiktok-icon.png")
            st.image(tiktok_logo)
            
            st.markdown("""<a style='display: block; text-align: center;'>**These three are top artists on PH TikTok.**</a>""",unsafe_allow_html=True,)
    

def methodology():
    st.title('Methodology and Data Sources')
    methodology = Image.open("Sprint_2_G1_SB19FTW/Slide6.png")
    st.image(methodology)

def chart_perf():
    st.title('Chart Performance')
    st.subheader("How is SB19 doing on the charts?")
    sb19_charts = Image.open("img/sb19_chartpos.png")
    st.image(sb19_charts)
    st.write("")
    st.markdown(
            "The group debuted in 2018 with the ballad single *Tilaluha* but what catapulted them to the top was **Go Up** -- their 2019 breakout single. From then on their singles releases achieved better positions in the charts but haven't stay long in the charts compared to other artists."
        )
    st.markdown(
            "### We see 2 opportunities for SB19:"
        )
    st.markdown(
            "#### 1. Increase streams"
        )
    st.markdown(
            "#### 2. Become a mainstay in the charts"
        )

def tiktok():
    st.title('What is the TikTok Sound?')

def pitch():
    st.title('How can we use data science to help SB19?')
    

def recommender():
    st.title('The Recommender Engine')
    

def conclusion():
    st.title('How to we take P-Pop to the top?')

def references():
    st.title('References')
    
    st.subheader('[1] Building Better Learning Environments in the Philippines')
    st.write("World Bank Group. (2016). Building Better Learning Environments in the Philippines. Philippines education note,no. 4;. World Bank, Washington, DC. © World Bank. https://openknowledge.worldbank.org/handle/10986/24744 License: CC BY 3.0 IGO.")
    
    st.subheader("[2] House Bill No. 473: An Act Regulating Class Size in All Public Schools and Appointing Funds Therefor")
    st.write("Tinio, A. L., & Castro, F. L. (2016, June 30). House Bill No. 473: An Act Regulating Class Size in All Public Schools and Appointing Funds Therefor. House Bill No. 473. https://www.congress.gov.ph/legisdocs/basic_17/HB00473.pdf.")
    
    st.subheader("[3] Class-size affects students' learning : DepEd. Philippine News Agency RSS")
    st.write("Montemayor, M. T. (2018, March 19). Class-size affects students' learning : DepEd. Philippine News Agency RSS. https://www.pna.gov.ph/articles/1029281. ")

    st.subheader('[4] Enhanced Basic Education Information System (EBEIS) (2015)')
    st.write("")    

    st.subheader('[5] Comparing the DISADVANTAGE INDEX (DI) with GEOGRAPHICALLY ISOLATED AND DISADVANTAGED AREAS (GIDA)')
    st.write("Comparing the DISADVANTAGE INDEX (DI) with GEOGRAPHICALLY ISOLATED AND DISADVANTAGED AREAS (GIDA). DepEd, 2015.")      
    
    st.subheader('[6] Computation of Public Schools MOOE')
    st.write("Llego, M. A. (2015). Computation of Public Schools MOOE. https://www.teacherph.com/computation-public-schools-mooe/")  
    
    
    
list_of_pages = [
    "The Project",
    "Who is SB19?",
    "SB19 and Spotify",
    "Data Sources and Methodology",
    "SB19's Chart Performance",
    "The TikTok Sound",
    "The Pitch",
    "Genre Classifier and Recommender Engine",
    #"The Playlists",
    "Conclusion",
    "References"
]

st.sidebar.title('P-Pop to the Top!')
selection = st.sidebar.radio("Go to", list_of_pages)

if selection == "The Project":
    project()

elif selection == "Who is SB19?":
    sb19()

elif selection == "SB19 and Spotify":
    sb19_spotify()

elif selection == "Data Sources and Methodology":
    methodology()

elif selection == "SB19's Chart Performance":
    chart_perf()

elif selection == "The TikTok Sound":
    tiktok()

elif selection == "The Pitch":
    pitch()

elif selection == "Genre Classifier and Recommender Engine":
    recommender()

elif selection == "Conclusion and Recommendations":
    conclusion()
    
elif selection == "References":
    references()
