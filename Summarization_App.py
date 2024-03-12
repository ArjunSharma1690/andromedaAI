import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader
from gensim.summarization import summarize
import time
import spacy
nlp = spacy.load('en_core_web_sm')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import string

st.set_page_config(layout = "wide")

# txtai Summarizer Code Starts:

@st.cache_resource
def text_summary(text, maxlength = None):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result
    
def extract_txt_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

def gen_summary(text):
    return summarize(text)

def readingTime(text):
	total_words = len([ token.text for token in nlp(text)])
	estimatedTime = total_words / 200.0
	return estimatedTime

def word_count_tokenizer(text):
    tokens = word_tokenize(text)
    return tokens

def sentence_count_tokenizer(text):
    sent_tokens = sent_tokenize(text)
    return sent_tokens

def list_to_str(text):
    listToStr = len(text)
    return listToStr

# clear function
# def Clear():
#     pyautogui.press("tab", interval = 0.15)
#     pyautogui.hotkey("ctrl", "a",'del', interval = 0.15)
#     pyautogui.press("tab", interval = 0.15)


# def main():
choice = st.sidebar.selectbox("Select Summarizer Options", ["Text Summarizer", "Document Summarizer", "Extractive Summarizer"])
# st.sidebar.slider("Select Word Range for Summary Output", 25, 500)
# clear = st.button("CLEAR")
if choice == "Text Summarizer":
    start = time.time()
    st.subheader(":orange[Get your Content Summarized]")
    input_text = st.text_area("**:blue[Enter your Text here!!]**")
    if st.button("Summarize Text"):
        if input_text == '':
            st.warning("Sorry, We cannot process Emptyness as of Now, Please input something!!")
# else:
#     start = time.time()
#     st.subheader("Get your Content Summarized")
#     input_text = st.text_area("Enter you Text here!!")
#     if st.button("Summarize Text"):
        elif input_text != '': 
            # st.button("Summarize Text")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**:orange[Your Input Text]** :pencil:")
                reading_time = readingTime(input_text)
                st.markdown(f"Reading Time :  {reading_time}")
                # st.markdown("Reading Time: {}" .format(reading_time)) #For single line printing
                # st.markdown(reading_time)
                st.info(input_text)
                tokens = word_count_tokenizer(input_text)
                #'''Remove Punctuation'''
                no_punct_tokens = [''.join(character for character in word
                                           if character not in string.punctuation)
                                           for word in tokens if word]
                #'''Remove '' from above generated output '''
                no_punct_tokens = [word.translate(string.punctuation) for word in no_punct_tokens if word]
                # st.markdown(no_punct_tokens)
                lst_to_str = str(input_text)
                tokens = word_count_tokenizer(input_text)
                #'''Remove Punctuation'''
                no_punct_tokens = [''.join(character for character in word
                                           if character not in string.punctuation)
                                           for word in tokens if word]
                #'''Remove '' from above generated output '''
                no_punct_tokens = [word.translate(string.punctuation) for word in no_punct_tokens if word]
                # st.markdown(no_punct_tokens)
                st.markdown('Total Natural Words in Corpus = {}' .format(len(no_punct_tokens)))
                snt_tokens = sentence_count_tokenizer(input_text)
                st.markdown('Total Sentences in Corpus = {}' .format(len(snt_tokens)))
                lst_to_str = str(input_text)
                st.markdown('Total Characters in Corpus = {}' .format(len(lst_to_str)))
            with col2:
                st.markdown("**:orange[Summarized Text]** :pencil:")
                result = text_summary(input_text)
                # st.markdown("Reading Time:")
                summary_reading_time = readingTime(result)
                st.markdown(f"Reading Time :  {summary_reading_time}")
                end = time.time()
                final_time = end - start
                # st.markdown(summary_reading_time)
                st.success(result)
                tokens = word_count_tokenizer(result)
                #'''Remove Punctuation'''
                no_punct_tokens = [''.join(character for character in word
                                           if character not in string.punctuation)
                                           for word in tokens if word]
                #'''Remove '' from above generated output '''
                no_punct_tokens = [word.translate(string.punctuation) for word in no_punct_tokens if word]
                # st.markdown(no_punct_tokens)
                st.markdown('Total Natural Words after Generation = {}' .format(len(no_punct_tokens)))
                snt_tokens = sentence_count_tokenizer(result)
                st.markdown('Total Sentences after Generation = {}' .format(len(snt_tokens)))
                lst_to_str = str(result)
                st.markdown('Total Characters in Generated Corpus = {}' .format(len(lst_to_str)))

if choice == "Document Summarizer":
    st.subheader("**:orange[Summarize your Document]**")
    input_file = st.file_uploader("**:blue[Upload your Document]**", type = ["pdf"])
    if st.button("Summarize Document"):
        if input_file is None:
            st.error("You need to a upload a choice of Document!!")
        #Check Dynamic nature of file
        else:
            with open("doc_summ_file_sample.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**:orange[Extracted Text from the Document]**")
                extracted_txt = extract_txt_from_pdf("doc_summ_file_sample.pdf")
                reading_time = readingTime(extracted_txt)
                st.markdown(f"Reading Time :  {reading_time}")
                # st.markdown(reading_time)
                st.info(extracted_txt)
            with col2:
                # result = extract_txt_from_pdf("doc_file.pdf")
                result = extracted_txt
                st.markdown("**:orange[Summarized Document]**")
                summary_result = text_summary(result)
                reading_time = readingTime(summary_result)
                st.markdown(f"Reading Time :  {reading_time}")
                # st.markdown(reading_time)
                st.success(summary_result)
            
if choice == "Extractive Summarizer":
    start = time.time()
    st.subheader("**:orange[Get your Content Summarized]**")
    gen_input_text = st.text_area("**:blue[Enter you Text here!!]**")
    if st.button("Text Summarize"):
        if gen_input_text == '':
            st.warning("Sorry, We cannot process Emptyness as of Now, Please input something!!")
# else:
#     start = time.time()
#     st.subheader("Get your Content Summarized")
#     input_text = st.text_area("Enter you Text here!!")
#     if st.button("Text Summarize"):
        elif gen_input_text != '': 
            # st.button("Summarize Text")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**:orange[Your Input Text]**")
                reading_time = readingTime(gen_input_text)
                st.markdown(f"Reading Time :  {reading_time}")
                # st.markdown(reading_time)
                st.info(gen_input_text)
            with col2:
                st.markdown("**:orange[Summarized Text]**")
                result = gen_summary(gen_input_text)
                # st.markdown("Reading Time:")
                summary_reading_time = readingTime(result)
                end = time.time()
                final_time = end - start
                st.markdown(f"Reading Time : {summary_reading_time}")
                st.success(result)
                
                
# # if __name__ == "__main__":
# #     main()

# # txtai Summarizer Code Ends!!

# # def summary(text):
# #     return summarize(text)

# # activites = ["Text Summarizer"]
# # choice1 = st.sidebar.selectbox("Extractive Summarizer", activites)
# # if choice1 == "Text Summarizer":
# # #         html_temp = """<div style="background-color:default;">
# # #         <h1 style='text-align: left; color: white;'>Get Your Text Summary</h1>
# # #         </div>"""
# # #         components.html(html_temp)
# #     st.markdown("Extractive Summarization")
# #     text = st.text_area("Transform Your Text", height = 300, placeholder = 'Give me some data!!')
# #     text_range= st.sidebar.slider("Select Word Range for Summary Output", 25, 500)
# #     if st.button("summarize"):
# #         st.success(summary(text))
#     # text_range= st.sidebar.slider("Select Word Range for Summary Output", 25, 500)
#     # text = st.text_area("Transform Your Text", height = 250)
#     # if st.button("summarize1"):
#     #     st.warning(summarize(text,word_count = text_range))