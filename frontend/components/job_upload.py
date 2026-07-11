import streamlit as st


def render_job_upload():

    st.header("Job Description")

    st.caption(
        "Upload the job description that candidates will be evaluated against."
    )

    return st.file_uploader(
        "Upload a job description",
        type=[
            "pdf",
            "docx",
            "txt",
        ],
    )