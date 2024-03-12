import streamlit as st

#NLP Packages
import spacy_streamlit
import spacy
nlp = spacy.load('en_core_web_sm')

#Web Scraping Packages
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# FUNCTION TO FETCH CONTENT FROM URL

# @st.cache
# def get_text(raw_url):
#     page = urlopen(raw_url)
#     soup = BeautifulSoup(page)
#     fetched_text = " ".join(map(lambda p:p.text, soup.find_all('p')))
#     return fetched_text

def main():
    """A Simple NLP App with Spacy-Streamlit"""
    st.subheader("**:orange[Named Entity Recognition Application]**")
    choice = st.sidebar.selectbox("**:violet[NER Options]**", ["Text NER"])#"Document NER" --> PENDING
    if choice == "Text NER":
        menu = ["NER", "Token Tags"]
        choice_rad = st.sidebar.radio("Pick a choice", menu)
        if choice_rad == "NER":
            global raw_text
            raw_text = st.text_area("**:blue[Add your Text here]**", key = "ner_text")
            # st.button("Produce")
            if raw_text == "":
                pass
                if st.button("Identify Entities"):
                    st.warning("Please Input some data for Processing to take place!!")
            elif raw_text != "":
                docx = nlp(raw_text)
                spacy_streamlit.visualize_ner(docx, labels = nlp.get_pipe('ner').labels)
                # st.button("clear text input", on_click=clear_text)
                # st.write(raw_text)
        if choice_rad == "Token Tags":
            global raw_text_token
            raw_text_token = st.text_area("**:blue[Add your Text here]**", key = "token_text")
            # st.button("Produce")
            if raw_text_token == "":
                pass
                if st.button("Produce Tokens"):
                    st.warning("Please Input some data for Processing to take place!!")
            elif raw_text_token != "":
                docx = nlp(raw_text_token)
                a = spacy_streamlit.visualize_tokens(docx, attrs = ['text', 'pos_', 'ent_type_']) #'dep_'

# URL NER
    # if choice == "NER":
    #     raw_text = st.text_area("Enter Text","")
    #     if raw_text != "":
    #         docx = nlp(raw_text)
    #         spacy_streamlit.visualize_ner(docx, labels = nlp.get_pipe('ner').labels)

    # # elif choice == "NER for URL":
    # #     raw_url = st.text_input("Enter URL","")
    # #     text_length = st.slider("Length to Preview", 50,200)
    # #     if raw_url != "":
    # #         result = get_text(raw_url)
    # #         len_of_full_text = len(result)
    # #         len_of_short_text = round(len(result)/text_length)
    # #         st.subheader("Text to be analyzed:")
    # #         st.write(result[:len_of_short_text])
    # #         preview_docx = nlp(result[:len_of_short_text])
    # #         spacy_streamlit.visualize_ner(preview_docx, labels = nlp.get_pipe('ner').labels)

if __name__ == '__main__':
    main()

# CLEAR FUNCTION FOR NER RADIO OPTION
def ner_clear_text():
    st.session_state["ner_text"] = ""
    st.session_state["token_text"] = ""

st.button("Click to Clear", on_click = ner_clear_text)

# # CLEAR FUNCTION FOR TOKEN TAGS RADIO OPTION
# def token_clear_text():
#     st.session_state["token_text"] = ""

# st.button("Click and Clear", on_click = token_clear_text)
# st.write(raw_text)
