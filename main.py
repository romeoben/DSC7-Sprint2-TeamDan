import warnings
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import streamlit.components.v1 as components
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

    intro_image = Image.open('img/Slide1.PNG')

    col1, col2 = st.beta_columns(2)
    with col1:
        st.image(intro_image)
    with col2:
        st.write("")
        st.write("")
        st.markdown(
            "# We harnessed the power of data to decode the **TikTok** sound and inspire **SB19’s** new hit track designed to *top the charts*."
        )

     
def sb19():
    st.title('Introducing SB19')
    st.write("")
    st.subheader(
            "Meet Josh, Pablo, Stell, Ken, and Justin"
        )
    col1, col2 = st.beta_columns(2)
    with col1:
        sb19_pic = Image.open('img/Slide2.PNG')
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


def sb19_spotify():
    st.title('SB19 and Spotify: At A Glance')

    col1, col2 = st.beta_columns(2)
    with col1:
        sb19_follow = Image.open("img/Slide3.PNG")
        st.image(sb19_follow)
        st.markdown(
            "SB19 has a **massive following** on social media but **relatively low streams** on Spotify."
        )
    with col2:
        tiktok_follow = Image.open("img/Slide4.PNG")
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
    methodology = Image.open("img/Slide6.PNG")
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
    st.subheader("TikTok Artists Chart Performance")
    tiktok_charts = Image.open("img/tiktok_chartpos.png")
    st.image(tiktok_charts)
    st.write("")
    col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
    with col1:
        img = Image.open("img/matthaios.jpg")
        st.image(img)
    with col2:
        st.write("")
        st.markdown(
            "### MATTHAIOS"
        )
        st.markdown(
            "#### Binibini"
        )
        st.markdown(
            "#### 24M Streams"
        )
    with col3:
        img = Image.open("img/juancaoile.jfif")
        st.image(img, use_column_width=True)
    with col4:
        st.write("")
        st.markdown(
            "### JUAN CAOILE"
        )
        st.markdown(
            "#### Marikit"
        )
        st.markdown(
            "#### 43M Streams"
        )
    with col5:
        img = Image.open("img/lilvinceyy.jpg")
        st.image(img)
    with col6:
        st.write("")
        st.markdown(
            "### LIL VINCEYY"
        )
        st.markdown(
            "#### Chinita Girl"
        )
        st.markdown(
            "#### 25M Streams"
        )
    st.markdown(
            "*Binibini*, *Chinita Girls*, and *Marikit* were all released in the first quarter of 2020 and maintained high Spotify chart positions for most of that year. **What are these TikTok artists and their songs doing right?**"
        )
    col1, col2 = st.beta_columns(2)
    with col1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
            "We looked into the audio features of global vs. local vs. TikTok songs charting in the Top 200. We found that TikTok follows a similar formula when it comes to their songs: **loud, fast-paced, and danceable songs with minimal lyrics.**"
        )
        st.markdown(
            "From here, we can say that TikTok has created **its own signature sound.**"
        )
    with col2:    
        option = st.selectbox('Select an audio feature:',
            ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'], key = "0000")
            
        if option == "danceability":
            img = Image.open("tiktok_features/dance.png")
            st.image(img)
            
        elif option == "energy":
            img = Image.open("tiktok_features/energy.png")
            st.image(img)

        elif option == "loudness":
            img = Image.open("tiktok_features/loud.png")
            st.image(img)
            
        elif option == "speechiness":
            img = Image.open("tiktok_features/speech.png")
            st.image(img)
            
        elif option == "acousticness":
            img = Image.open("tiktok_features/acoustic.png")
            st.image(img)
            
        elif option == "instrumentalness":
            img = Image.open("tiktok_features/instrum.png")
            st.image(img)
            
        elif option == "liveness":
            img = Image.open("tiktok_features/live.png")
            st.image(img)
            
        elif option == "valence":
            img = Image.open("tiktok_features/val.png")
            st.image(img)
            
        elif option == "tempo":
            img = Image.open("tiktok_features/tempo.png")
            st.image(img)
    
    st.subheader("So how does SB19 compare?")
    col1, col2 = st.beta_columns(2)
    with col1:
        option1 = st.selectbox('Select an audio feature:',
            ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'], key = "0001")
            
        if option1 == "danceability":
            img = Image.open("sb19_v_tiktok/dance.png")
            st.image(img)
            
        elif option1 == "energy":
            img = Image.open("sb19_v_tiktok/energy.png")
            st.image(img)

        elif option1 == "loudness":
            img = Image.open("sb19_v_tiktok/loud.png")
            st.image(img)
            
        elif option1 == "speechiness":
            img = Image.open("sb19_v_tiktok/speech.png")
            st.image(img)
            
        elif option1 == "acousticness":
            img = Image.open("sb19_v_tiktok/acoustic.png")
            st.image(img)
            
        elif option1 == "instrumentalness":
            img = Image.open("sb19_v_tiktok/instrum.png")
            st.image(img)
            
        elif option1 == "liveness":
            img = Image.open("sb19_v_tiktok/live.png")
            st.image(img)
            
        elif option1 == "valence":
            img = Image.open("sb19_v_tiktok/val.png")
            st.image(img)
            
        elif option1 == "tempo":
            img = Image.open("sb19_v_tiktok/tempo.png")
            st.image(img)
    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
            "Let's compare SB19’s sound to that of mainstay Tiktok songs. The team defined mainstay songs to be those which charted in top 20 and stayed in charts for at least a year. Mainly, we can see that SB19 songs tends to be **less danceable, generally louder, and more likely to be performed live** than the current TikTok sound."
        )


def pitch():
    st.title('How can we use data science to help SB19?')
    col1, col2 = st.beta_columns(2)
    with col1:
        alt1 = Image.open("img/Slide12.PNG")
        st.image(alt1)
    with col2:
        alt2 = Image.open("img/Slide13.PNG")
        st.image(alt2)

def recommender():
    st.title('The Recommender Engine')
    
def playlists():
    st.title('The Playlists')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.markdown(
            "### Playlist 1: SB19’s New Sound"
        )
        st.markdown(
            "Seed Track: *Vibe With Me by Matthiaos*"
        )
        components.iframe("https://open.spotify.com/embed/track/0G5qmu4TsdUH19zdcbI9Ui", height=80)
        components.iframe("https://open.spotify.com/embed/playlist/46AnEzYNyAJGwCHQRG5IT8", height=380, scrolling=True)
        st.markdown(
            "*Vibe With Me* was chosen due"
        )
        img = Image.open("img/Slide16.PNG")
        st.image(img)
        
    with col2:
        st.markdown(
            "### Playlist 2: SB19’s Signature TikTok Sound"
        )
        st.markdown(
            "Seed Track: *Love Goes - EDM Version by SB19*"
        )
        components.iframe("https://open.spotify.com/embed/track/0LAh3hfeuUekvLm3Nq6MmA", height=80)
        components.iframe("https://open.spotify.com/embed/playlist/2Ih50y8D9X4ABq6NQZsMCJ", height=380, scrolling=True)
        st.markdown(
            "*Love Goes - EDM Version* was chosen as the seed track due to its **high TikTok probability (0.5)**, based on our classifier model."
        )
        img = Image.open("img/Slide20.PNG")
        st.image(img)
        
def conclusion():
    st.title('Conclusion and Recommendations')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.subheader('So, how do we take P-Pop to the top?')
        img = Image.open("img/Slide21.PNG")
        st.image(img)
            
    with col2:
        st.subheader('We\'re off to a great start, but what can we do better?')
        img = Image.open("img/Slide22.PNG")
        st.image(img)

def references():
    st.title('References')
    
    st.markdown('#### 1. TikTok. (2019, August 16). *This year on TikTok: Celebrating the community and videos that brought Filipinos together in 2020.* Newsroom. https://newsroom.tiktok.com/fil-ph/tiktok-top-100-list-for-the-philippines. ')
    st.markdown('#### 2. GMA News Online. (2020, November 23). *5 Pinoy hip-hop artists to listen to, according to Matthaios.* GMA News Online. https://www.gmanetwork.com/news/lifestyle/hobbiesandactivities/765254/matthaios-recommends-listening-to-these-5-pinoy-hip-hop-artists/story/. ')
    st.markdown('#### 3. ABS-CBN News, &amp; Salterio, L. C. (2020, July 18). *How \'Marikit\' became a massive hit for newcomer Juan Caoile.* ABS. https://news.abs-cbn.com/entertainment/07/18/20/how-marikit-became-a-massive-hit-for-newcomer-juan-caoile. ')

    
    
    
list_of_pages = [
    "The Project",
    "Who is SB19?",
    "SB19 and Spotify",
    "Data Sources and Methodology",
    "SB19's Chart Performance",
    "The TikTok Sound",
    "The Pitch",
    "Genre Classifier and Recommender Engine",
    "The Playlists",
    "Conclusion and Recommendations",
    "References"
]

st.sidebar.title('P-Pop to the Top!')
sb19_logo = Image.open('img/SB19_OfficialLogo.jpg')
st.sidebar.image(sb19_logo, caption='', width = 200)
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

elif selection == "The Playlists":
    playlists()

elif selection == "Conclusion and Recommendations":
    conclusion()
    
elif selection == "References":
    references()
