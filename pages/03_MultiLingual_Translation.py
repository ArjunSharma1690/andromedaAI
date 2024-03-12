import streamlit as st
from mtranslate import translate
import pandas as pd
import os
import pyautogui
from PyPDF2 import PdfReader
import spacy
nlp = spacy.load('en_core_web_sm')

# read language dataset
df = pd.read_excel('language.xlsx', sheet_name = "selected")
lang = df['Language'].to_list()
langlist=tuple(lang)
langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# layout
st.subheader("**:orange[Language Translation Application]**")
# st.title("Developer: arjun.sharma")

def extract_txt_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

# clear function
def Clear():
    pyautogui.press("tab", interval = 0.15)
    pyautogui.hotkey("ctrl", "a",'del', interval = 0.15)
    pyautogui.press("tab", interval = 0.15)
    
def readingTime(text):
	total_words = len([ token.text for token in nlp(text)])
	estimatedTime = total_words / 200.0
	return estimatedTime

opts = st.sidebar.selectbox("Select  Options", ["Input Translation", "Document Translation"])

if opts == "Input Translation":
    clear = st.button("CLEAR")
    choice = st.sidebar.radio('SELECT LANGUAGE', langlist)
    inputtext = st.text_area("**:blue[Add your Text here]**", height = 200)
    if len(inputtext) > 0 :
        reading_time = readingTime(inputtext)
        try:
            output = translate(inputtext, lang_array[choice])
            st.text_area("**:blue[Translated Version Below]**", output, height = 200)
        except Exception as e:
            # st.error(e)
            print()
elif opts == "Document Translation":
    input_file = st.file_uploader("**:blue[Upload your Document]**", type = ["pdf"])
    choice = st.sidebar.radio('SELECT LANGUAGE', langlist)
    if st.button("Translate Uploaded Document"):
        if input_file is None:
            st.warning("Please upload a relevant document!!")
        else:    
            with open("multi_lingu_file_sample.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1, 1])
            with col1:
                extracted_txt = extract_txt_from_pdf("multi_lingu_file_sample.pdf")
                st.markdown("**:orange[Original Language]**")
                st.info(extracted_txt)
            # choice = st.sidebar.radio('SELECT LANGUAGE', langlist)
            with col2:
                st.markdown("**:orange[Translated Version]**")
                output = translate(extracted_txt, lang_array[choice])
                st.info(output)
            # st.markdown(type(output))
            st.download_button(label = 'Download Converted File', data = output, file_name = "translated.txt")
        
    
# st.sidebar.slider("Select Word Range for Summary Output", 25, 500)

# clear = st.button("CLEAR")
# inputtext = st.text_area("INPUT", height = 200)
# choice = st.sidebar.radio('SELECT LANGUAGE', langlist)

# # clear function
# def Clear():
#     pyautogui.press("tab", interval = 0.15)
#     pyautogui.hotkey("ctrl", "a",'del', interval = 0.15)
#     pyautogui.press("tab", interval = 0.15)

# I/O
# if len(inputtext) > 0 :
#     try:
#         output = translate(inputtext, lang_array[choice])
#         st.text_area("TRANSLATED TEXT", output, height = 200)
#     except Exception as e:
#         st.error(e)

# Clear I/O
# if clear:
#     Clear()









# import streamlit as st

# from textblob import TextBlob

# from googletrans import Translator

# import os

# import streamlit.components.v1 as components

# def main():
#     st.title("This part of the Application will help you translate you data")
#     # st.write("hello")
#     activities = ["Multilingual_Translator"]
#     choice = st.sidebar.selectbox("Select Activities", activities)
#     if choice == "Multilingual_Translator":
#         from_text = st.text_input("Enter you Input")
#         from_code = st.text_input("Enter Conversion Code")
#         if st.button("Translate"):
#             translator = Translator()
#             try:
#                 a = (translator.translate(from_text, dest = from_code).text)
#                 st.success(a)
#             except Exception as e:
#                 a1 = os.system("ping www.google.com")
#                 if a == 1:
#                     st.write("please")
#                 else:
#                     st.write("wong")

# def main():
#     st.title("This part of the Application will help you translate you data")
#     # st.write("hello")
#     activities = ["Multilingual_Translator"]
#     choice = st.sidebar.selectbox("Select Activities", activities)
#     if choice == "Multilingual_Translator":
#         from_text = st.text_input("Enter you Input")
#         from_code = st.text_input("Enter Conversion Code")
#         tanslator = Translator()
#         a = (tanslator.translate(from_text, dest = from_code).text)
#         st.success(a)
        
       
    
    
# if __name__ == '__main__':
#     main()





# def main():
#     activites = ["Translator"]
#     choice = st.sidebar.selectbox("Select the Desired Functionality", activites)
#     if choice == "Translator":
#         html_temp3 = """<div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Text Translator</p></div>""" 
#         components.html(html_temp3)
#         blob = TextBlob("Comment vas-tu?")
#         # print(blob.translate(to = 'es'))
#         row_text = st.text_area("Enter Your Text For Translation",height=300)
#         translation_text = TextBlob(row_text)
#         list1 = ["en","ta","pa","gu","hi","ur","kn","bn","te"]
#         a = st.selectbox("select",list1)
#         if st.button("search"):
#             # input1 = TextBlob("Simple is better than complex")
#             st.info(translation_text.translate(to = a))
            
# if __name__ == '__main__':
#     main()