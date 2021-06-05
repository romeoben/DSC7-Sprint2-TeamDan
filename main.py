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

    intro_image = Image.open('img/Sprint_2_G1_SB19 FTW/Slide1.png')

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
        sb19_pic = Image.open('img/Sprint_2_G1_SB19 FTW/Slide2.png')
        st.image(sb19_pic)
    with col2:
        st.markdown(
            " - Trained for 3 years by ShowBT Philippines",
            " - Active since 2018",
            " - The first Filipino and Southeast Asian act to be nominated in **Billboard Music Awards** for the *Top Social Artist* category"
        )
    
    st.subheader(
            "On Social Media:"
        )
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.markdown('**Facebook**')
        st.write("**1.4M Followers**")

    with col2:
        st.subheader('**Twitter**')
        st.write("**422k Followers**")

    with col3:
        st.subheader('**Instagram**')
        st.write("**454K Followers**")


def data_method():
    st.title('Data Sources and Methodology')
    st.write("")
    col1, col2 = st.beta_columns(2)
    with col1:
        data_sources = Image.open("data_sources.png")
        st.image(data_sources)
    with col2:
        methodology = Image.open("methodology.png")
        st.image(methodology)

def methodology():
    st.title('Methodology and Data Sources')
    methodology = Image.open("img/Sprint_2_G1_SB19 FTW/Slide6.png")
    st.image(methodology)

def chart_perf():
    st.title('Chart Performance')
    st.subheader("What are these TikTok artists doing right?")
    st.write("")
    st.write("Correlation coefficient: 0.42")

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
    "Data Sources and Methodology",
    "SB19's Chart Performance",
    "The Pitch",
    "Genre Classifier and Recommender Engine",
    #"The Playlists",
    "Conclusion",
    "References"
]

st.sidebar.title('Table of Contents')
selection = st.sidebar.radio("Go to", list_of_pages)

if selection == "The Project":
    project()

elif selection == "Who is SB19?":
    sb19()

elif selection == "Data Sources and Methodology":
    data_method()

elif selection == "SB19's Chart Performance":
    chart_perf()

elif selection == "The Pitch":
    pitch()

elif selection == "Genre Classifier and Recommender Engine":
    recommender()

elif selection == "Conclusion and Recommendations":
    conclusion()
    
elif selection == "References":
    references()
