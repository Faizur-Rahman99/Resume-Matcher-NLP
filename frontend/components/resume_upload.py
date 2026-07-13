import streamlit as st


def render_resume_upload():
    """
    Render the resume uploader.
    """

    st.subheader("👤 Candidate Resumes")

    st.markdown(
        """
        Upload one or more candidate resumes
        for automatic ranking.
        """
    )

    return st.file_uploader(
        "Choose one or more resumes",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True,
    )