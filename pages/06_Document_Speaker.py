#Author : Arjun Sharma

import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS #pip install gTTs #--------------https://gtts.readthedocs.io/en/latest/module.html
import base64
from PyPDF2 import PdfReader

def extract_txt_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

def text_to_speech(input_language, output_language, text, tld):
    # translation = translator.translate(text, src=input_language, dest=output_language)
    # trans_text = translation.text
    tts = gTTS(extracted_txt, lang="en", tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text

# read language dataset
# df = pd.read_excel('language.xlsx', sheet_name = "text_trans_speak")
# lang = df['Language'].to_list()
# langlist=tuple(lang)
# langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
# lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}


# function to decode audio file for download
# def get_binary_file_downloader_html(bin_file, file_label='File'):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     bin_str = base64.b64encode(data).decode()
#     href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
#     return href

choice = st.sidebar.selectbox("Select Options", ["Document Speaker"])

speech_langs = {"en": "English"}

tld_dict = {}

# english_accent = st.radio(
#     "Select your english accent",
#     (
#         "Default",
#         "India",
#         "United Kingdom",
#         "United States",
#         "Canada",
#         "Australia",
#         "Ireland",
#         "South Africa",
#     ),
# )

# accent_list = ("com.au")

if choice == "Document Speaker":
    st.subheader("**:orange[Speak For Me in Desired Accent]**")
    input_file = st.file_uploader("**:blue[Upload your Document]**", type = ["pdf"])
    if st.button("Listen To Your Document"):
        if input_file is None:
            st.error("You need to a upload a choice of Document!!")
        #Check Dynamic nature of file
        else:
            with open("doc_file_doc_speaker.pdf", "wb") as f:
                f.write(input_file.getbuffer())
                # '''For now st.columns is also behaving like st.beta_columns'''
            col1, col2, col3 = st.columns([1, 0.5, 1])#creates 3 columns where the first column is 3 times the width of the second, and the last column is 2 times that width.
            #'''st.beta_columns will be removed soon, if Error comes, revert to st.columns'''
            # col1, col2, col3 = st.beta_columns([1, 0.5, 1])
            #'''Uncomment below and Comment above line to put the play button at the Bottom'''
            #'''And take the code out of Col3 condition'''
            # col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**:orange[Read Text from the Document]**")
                extracted_txt = extract_txt_from_pdf("doc_file_doc_speaker.pdf")
                # reading_time = readingTime(extracted_txt)
                # st.markdown("Reading Time:")
                # st.markdown(reading_time)
                st.success(extracted_txt)
            with col2:
                accent = st.radio("**:orange[Select English Accent]**", 
                                  ("Indian", "USA", "British", "Canadian", 
                                   "South African", "Ireland", "Australia"))
                    # st.markdown("yo")
            with col3:
                if accent == "Indian": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "co.in")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                if accent == "USA": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "us")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                if accent == "British": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "co.uk")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                if accent == "Canadian": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "ca")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                if accent == "South African": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "co.za")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                if accent == "Ireland": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "ie")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                if accent == "Australia": 
                    aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "com.au")
                    aud_file.save("lang.mp3")
                    audio_file_read = open('lang.mp3', 'rb')
                    audio_bytes = audio_file_read.read()
                    bin_str = base64.b64encode(audio_bytes).decode()
                    st.markdown("**:orange[Play Me]**")
                    st.audio(audio_bytes, format='audio/mp3')
                # st.radio("select accent", ("U"),):
                #     # st.markdown("yo")
                #     aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "com")
                #     aud_file.save("lang.mp3")
                #     audio_file_read = open('lang.mp3', 'rb')
                #     audio_bytes = audio_file_read.read()
                #     bin_str = base64.b64encode(audio_bytes).decode()
                #     st.markdown("Play Me")
                #     st.audio(audio_bytes, format='audio/mp3')
            #     english_accent = st.radio(
            #         "Select your english accent",
            #             (
            #             "Default",
            #             "India",
            #             "United Kingdom",
            #             "United States",
            #             "Canada",
            #             "Australia",
            #             "Ireland",
            #             "South Africa",
            #             ),
            #         )
            #     if english_accent == "Default":
            #         tld = "com"
            #     elif english_accent == "India":
            #         tld = "co.in"
            #     elif english_accent == "United Kingdom":
            #         tld = "co.uk"
            #     elif english_accent == "United States":
            #         tld = "com"
            #     elif english_accent == "Canada":
            #         tld = "ca"
            #     elif english_accent == "Australia":
            #         tld = "com.au"
            #     elif english_accent == "Ireland":
            #         tld = "ie"
            #     elif english_accent == "South Africa":
            #         tld = "co.za"
            # with col3:
            #     st.markdown("Processing!!")
            #     if len(extracted_txt) > 0 :
            #         aud_file = gTTS(text = extracted_txt, lang = "en", slow = False, tld = "com.au")
            #         aud_file.save("lang.mp3")
            #         audio_file_read = open('lang.mp3', 'rb')
            #         audio_bytes = audio_file_read.read()
            #         bin_str = base64.b64encode(audio_bytes).decode()
            #         st.markdown("Play Me")
            #         st.audio(audio_bytes, format='audio/mp3')


