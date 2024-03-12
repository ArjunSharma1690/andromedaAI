import streamlit as st
from fpdf import FPDF
import base64

input_text = st.text_area("**:orange[Enter your Text]**")

export_to_pdf = st.button("Export PDF")

###Currently it is not possibe to Download file to a Custom Directory###

# download_path = r'C:/Users/ARJUN SHARMA/Desktop/Data_Science_PDFs_and_algos/dockers_master/plagiarism/new'

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    # file_name = st.text_input("Enter a file name:", "")
    # st.write("You entered:", file_name)
    return f'<a href = "data:application/octet-stream; base64, {b64.decode()}" download = "{filename}.pdf">Download file</a>'

# if __name__ == "__create_download_link__":
#     create_download_link()

if export_to_pdf:
    pdf = FPDF()
    pdf.add_page()
    # pdf.set_font('Arial', 'B', 16) #Bold
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, input_text) #useful when you want to add paragraphs of text to a PDF document while automatically handling line breaks and text wrapping.
    # pdf.cell(40, 10, input_text)
    
    # html = create_download_link(pdf.output(dest = download_path).encode("latin-1"), "test")
    html = create_download_link(pdf.output(dest = "S").encode("latin-1"), "test")
    # file_name = html
    # html = st.text_input("Enter a file name:", "")
    # st.write("You entered:", html)

    st.markdown(html, unsafe_allow_html = True)
    
# def main():
#     # st.title("Download PDF Example")

#     # Generate some PDF content (replace this with your own PDF generation code)
#     pdf_content = b"input_text"

#     # Get the user's input for the file name
#     file_name = st.text_input("Enter a file name:", "my_pdf")

#     # Create a download link
#     download_link = create_download_link(pdf_content, file_name)
#     st.markdown(download_link, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()