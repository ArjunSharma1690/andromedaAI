from __future__ import absolute_import, print_function
import streamlit as st
import nltk
nltk.data.path.append('./pages/lang_dec_stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader

def extract_txt_from_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

def language_detector(text):
    """
    Input: text (string) which wants to know the language
    Output: language of the text

    It detects dannish, dutch, english, finnish, french, german,
    hungarian, italian, kazakh, norwegian, portuguese, russian,
    spanish, swedish and turkish.
    """

    # Split string in a list of tokens (words and punctuation)
    tokens = word_tokenize(text)
    # Put tokens in lowercase
    low_tokens = [token.lower() for token in tokens]
    # Set of unique tokens present in the text
    tokens_set = set(low_tokens)

    # Dictionary
    # keys: language
    # value: number of different stopwords present in the string
    score = {}

    for language in  stopwords.fileids(): # Iterate over the languages
        # Load stopwords for the language
        stops = set(stopwords.words(language))
        # Look for which stopwords appear in the text
        in_common = tokens_set.intersection(stops)
        # Store the number of stopwords present in the text into
        # the dictionary score
        score[language] = len(in_common)

    # Return language with more different stopwords present in the text
    return max(score, key=score.get)



if __name__ == '__main__':
    st.subheader("**:orange[Detect your Data's Language]**")
    input_file = st.file_uploader("**:blue[Upload your Document]**", type = ["pdf"])
    if st.button("Detect Language"):
        if input_file is None:
            st.error("Please upload a relevant document!!")
        else:    
            with open("sample_lang_dec.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1,2])
            with col1:
                st.markdown("**:orange[Your Data in Uploaded File]**")
                extracted_txt = extract_txt_from_pdf("sample_lang_dec.pdf")
                # reading_time = readingTime(extracted_txt)
                # st.markdown("Reading Time:")
                # st.markdown(reading_time)
                st.info(extracted_txt)
            with col2:
                st.markdown("**:orange[Language in the Document is:]**")
                extracted_txt = extract_txt_from_pdf("sample_lang_dec.pdf")
                if language_detector(extracted_txt) == 'hinglish':
                    st.markdown("**:green[English]**")
                elif language_detector(extracted_txt) == 'arabic': #By default Arabic was showing, and I donot have Araboc in my stopword list file
                    pass
                else:
                    st.markdown(language_detector(extracted_txt))
                # print(language_detector(text))
                st.markdown("**:blue[If you wish to Translate you data into another Language, Please use **:red[Andromeda's]** Translation Functionality]** :thumbsup:")






# '''Text Code
# '''
# def language_detector(text):
#     """
#     Input: text (string) which wants to know the language
#     Output: language of the text

#     It detects dannish, dutch, english, finnish, french, german,
#     hungarian, italian, kazakh, norwegian, portuguese, russian,
#     spanish, swedish and turkish.
#     """

#     # Split string in a list of tokens (words and punctuation)
#     tokens = word_tokenize(text)
#     # Put tokens in lowercase
#     low_tokens = [token.lower() for token in tokens]
#     # Set of unique tokens present in the text
#     tokens_set = set(low_tokens)

#     # Dictionary
#     # keys: language
#     # value: number of different stopwords present in the string
#     score = {}

#     for language in  stopwords.fileids(): # Iterate over the languages
#         # Load stopwords for the language
#         stops = set(stopwords.words(language))
#         # Look for which stopwords appear in the text
#         in_common = tokens_set.intersection(stops)
#         # Store the number of stopwords present in the text into
#         # the dictionary score
#         score[language] = len(in_common)

#     # Return language with more different stopwords present in the text
#     return max(score, key=score.get)

# input_text = st.text_area("Enter you Text here!!")
# # text = "woman"

# if language_detector(input_text) == 'hinglish':
#     st.markdown('English')
# elif language_detector(input_text) == 'arabic':
#     pass
# else:
#     st.markdown(language_detector(input_text))
# # print(language_detector(text))