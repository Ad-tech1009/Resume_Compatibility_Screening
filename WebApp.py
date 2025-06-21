import streamlit as st
from pypdf import PdfReader
from utils.getScore(API) import get_score
from utils.printScore import display_score_gauge, display_strength_weakness, display_suggestions

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

if "desc" not in st.session_state:
    st.session_state['desc'] = None
if "reader" not in st.session_state:
    st.session_state['reader'] = None

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
    st.success("Job Description Submitted Successfully.")
  else:
    st.error("Please Enter Job Description.")

st.write("\n")

with st.form('resume'):
  resume_file = st.file_uploader(r"$\textsf{\large Upload Resume: }$", type="pdf")
  submit_button2 = st.form_submit_button(label='Submit')

if submit_button2:
  if resume_file:
    reader = read_pdf(resume_file)
    st.success("Resume Submitted Succesfully.")
  else:
    st.error("Please Upload Resume.")

if st.session_state['reader'] and st.session_state['desc']:
  col1, col2, col3 = st.columns([6, 1, 1])
  with col3:
    get_score_button = st.button("Get Score")
  st.markdown("---")

  if get_score_button:
    score, strength, weakness, suggestions = get_score(st.session_state['desc'],st.session_state['reader'])
    display_score_gauge(score)
    display_strength_weakness(strength,weakness)
    display_suggestions(suggestions)
