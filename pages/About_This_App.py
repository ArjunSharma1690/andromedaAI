import streamlit as st

import json

import requests

import streamlit_lottie as st_lottiee

# from typing_extensions import Literal

from typing_extensions import Literal as st_lottie

import os
# os.chdir("C:/Users/ARJUN SHARMA/Desktop/Data_Science_PDFs_and_algos/dockers_master/plagiarism/new/")

from streamlit_card import card

import base64

# import Literal as st_lottie

# st.markdown(os.getcwd())

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html = True,
)

st.subheader("**:violet[Welcome to Andromeda]**")
# st.markdown(
#     "<h2 style = 'text-align:center;'>Welcome to Andromeda</h2>", unsafe_allow_html = True
# )

st.write("")

def create_card(title, content):
    # st.write("---")
    st.write(f"#### {title}")
    st.write(content)
    st.write("---")
# Usage
create_card("Data Summarization", "Get the Summary of your Text")

create_card("Data Entities", "Identify various Entities in your Text")

create_card("Multi-Lingual Translation", "Get your data Translated into various Languages!!")

create_card("Spell Corrector", "Correct Spelling Mistakes!!")

create_card("Document Converter", "Export your Text into PDF Format")

create_card("Text to Speech", "Translate your Text into Another Language! Play The Translated Version! Download The Translated File")

create_card("Document Speaker", "Listen to the Content of your PDF Document")

@st.cache_resource
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('Screenshot_1.png')


# from streamlit_card import card

# hasClicked = card(
#   title="Hello World!",
#   text="Some description",
#   image="http://placekitten.com/200/300",
#   on_click=lambda: print("Clicked!")
# )


##NOT USING LOTTIES CURRENTLY

# def load_lottiefile(filepath: str):
#     with open(filepath, encoding="utf8") as f:
#         return json.load(f)
# os.chdir("C:/Users/ARJUN SHARMA/Desktop/Data_Science_PDFs_and_algos/dockers_master/plagiarism/new/pages/lottiefiles/")
# st.markdown(os.getcwd())
# lottie_coding = load_lottiefile("hello.json")  # replace link to local lottie file



# st_lottie(
#     lottie_coding,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="low", # medium ; high
#     renderer="svg", # canvas
#     height=None,
#     width=None,
#     key=None,
# )