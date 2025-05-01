import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="Resume Score Calculator", layout="wide")
st.markdown(
    "<h1 style='color: white; text-align: center; font-size: 56px'>Resume Score Calculator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h5 style='text-align: center; color: grey; font: Times New Roman;'>Instantly get Resume Score based on Job Description and get effective tips on improving your Resume!! </h5>",
            unsafe_allow_html=True
    )
st.markdown(
    f"""
    <style>
    .stApp {{background-color: black;}}
    </style>
    """,
    unsafe_allow_html=True
)

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text
  
with st.form('job_desc'):
	desc = st.text_area(r"$\textsf{\large Enter Job Description: }$")
	submit_button1 = st.form_submit_button(label='Submit')

if submit_button1:
  if desc:
    st.write("Job Description Submitted Successfully.")
    st.write(desc)
  else:
    st.write("Please Enter Job Description.")

st.write("\n")

with st.form('resume'):
  resume_file = st.file_uploader(r"$\textsf{\large Upload Resume: }$", type="pdf")
  submit_button2 = st.form_submit_button(label='Submit')

if submit_button2:
  if resume_file:
    reader = read_pdf(resume_file)
    st.write("Resume Submitted Succesfully.")
    st.write(reader)
  else:
    st.write("Please Upload Resume.")
