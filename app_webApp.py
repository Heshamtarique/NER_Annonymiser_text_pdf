#!/usr/bin/env python
# coding: utf-8

#import requests
import streamlit as st
#from streamlit_lottie import st_lottie
#from PIL import Image
from streamlit_option_menu import option_menu


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



# side bar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Work Experience", "Contact"])

if selected == "Home":
    st.title(f'Hi, I am Hesham :wave:')
    st.write("**My projects:**")
    st.write("On Going Project")
    st.write("* In the field of arrhythmia classification using ECG signals, several benchmark datasets have been utilized for research and evaluation purposes from physionet.org, (a) **MIT-BIH Arrhythmia Database**, (b) **PTB Database**, (c) **AF Classification Database**, and (d) **AF Termination Database**. Among the different models evaluated, the state-of-the-art (SOTA) Transformer model has shown exceptional performance. Compared to an LTSTM model built from scratch, the Transformer model achieves an impressive accuracy rate of 98.32 percent. This signifies the Transformer model's ability to effectively classify and detect different types of arrhythmias.")
    st.write("* BioNLP: In this project the medical data such as precription, lab reports will be used to build an AI model that can extract the Potential diseases, medicines and can be abel to recoommend the doctors/patients in more efficient way, making their tasks easy.")
    st.write("Completed Projects")
    st.write("* This paper proposes a real-time violence event identifier using state-of- the-art deep learning methods, including the Vision Transformer architecture. The model outperforms other explored models, achieving 98 percent accuracy on the RLVS dataset and 97 percent accuracy on the Hockey dataset. The study addresses the need for technology to automatically detect violence in surveillance footage and contributes to enhancing urban safety and aiding law enforcement. See my work here(https://dl.acm.org/doi/10.1145/3508072.3512288)")
    st.write("* Anonymizing texts using models from Spacy for two languages English and French. A webapp has been built using the spacy model that is able to extract the Name, Location etc. Text can be entred to the promp to  see the anonymized sentence and a pdf/word file can ablo be uploaded to get the location name etc anonymized. ")

if selected=="Contact":
    st.write("email: heshamtarique.jmi@gmail.com")
    st.write("mobile: 8766385285")

if selected=="Work Experience":
    st.write("Company: **Phenom**")
    
    st.write("14th Feb 2022 - 3rd March 2023")
    
    st.write("Position: Product Development Engineer {Search & Personalization Team}")
    
    st.write("* Experience Prediction & Job-Type Classification ModelPhenom Responsibilities Architected and Implemented job type and experience classification model based on job information data to boost up the profile recommendation system. Developed supervised experience prediction model using job title and description data to improve the complete profile ratio and filtering the suitable profile for recommendation/search system. Improved the ratio of the apply clicks by ~12%")
    
    st.write("* Development of Applies-based recommendation widget. Responsibilities. Architected and Implementing the recommendation of the job to the candidate based on past applies of the candidate. Developing a supervised model using the job title and must have skills and a description of the JD for training the data.")
    
    st.write("* Data Analysis of 2.4 million data from top four clients. The features which were explored are job type, job level, experience level, doamin of the job. These features were analysed so that required amount of data and features can be fed to the model.")
             

    st.write("Company: **siwe tech**")
    st.write("5th March 2023-Present")
    st.write("Position: Machine Learinng Engineer")
    st.write("On Going Project")
    st.write("* AI based chatBot development: This project is building an app which is utilizing Large Language Model GPT and top of it Reward Model is being used. ")
