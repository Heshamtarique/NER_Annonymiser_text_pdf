#!/usr/bin/env python
# coding: utf-8

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



# side bar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["home", "Projects", "Work Experience", "Contact"])

if selected == "home":
    st.title(f'Hi, I am Hesham :wave:')

if selected== "Projects":
    st.title("my projects are: ")
    st.write(
        "* I am passionate about finding ways to use Python and Deep Learning to be more efficient and effective in business settings."
    )
    st.write("* [This work was based on the classification of violent non-violent videos by using the deep learning model ViT[Vision Trasnformer]. This model is built on top of SOTA trasnformer by Google researchers.] We used two dataset Hockey_Fight_database and RLVS database fpr building the model. See my work here(https://dl.acm.org/doi/10.1145/3508072.3512288)")
    st.write("* Ongoing project: Multi_class Arrhythmia detection using SOTA transformer model. Here we are using MIT_BIH_Arrhythmia Database and PTB databse for the model building.")

if selected=="Contact":
    st.write("email: heshamtarique.jmi@gmail.com")
    st.write("mobile: 8766385285")

if selected=="Work Experience":
    st.write("Company: Phenom")
    st.write("Position: Product Development Engineer: ML")
    st.write("* Experience Prediction & Job-Type Classification ModelPhenom ResponsibilitiesHyderabad Architected and Implemented job type and experience classification model based on job information data to boost up the profile recommendation system. Developed supervised experience prediction model using job title and description data to improve the complete profile ratio and filtering the suitable profile for recommendation/search system. Improved the ratio of the apply clicks by ~12%")
    st.write("* Development of Applies-based recommendation widget. Responsibilities. Architected and Implementing the recommendation of the job to the candidate based on past applies of the candidate. Developing a supervised model using the job title and must have skills and a description of the JD for training the data.")










































