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
