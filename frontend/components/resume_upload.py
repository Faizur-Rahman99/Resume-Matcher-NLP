import streamlit as st


def render_resume_upload():

    st.header("Candidate Resumes")

    st.caption(
        "Upload one or more candidate resumes."
    )

    return st.file_uploader(
        "Upload candidate resumes",
        type=[
            "pdf",
            "docx",
            "txt",
        ],
        accept_multiple_files=True,
    )