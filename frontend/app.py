import streamlit as st


st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide",
)

st.title("AI Resume Matcher")

st.write(
    "Upload resumes and compare them against a job description."
)