import streamlit as st


def render_job_upload():
    """
    Render the job description uploader.
    """

    st.subheader("📄 Job Description")

    st.markdown(
        """
        Upload the job description that candidates
        will be evaluated against.
        """
    )

    return st.file_uploader(
        "Choose a job description",
        type=["pdf", "docx", "txt"],
    )