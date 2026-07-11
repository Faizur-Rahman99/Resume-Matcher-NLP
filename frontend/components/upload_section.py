import streamlit as st

from components.job_upload import render_job_upload
from components.resume_upload import render_resume_upload


def render_upload_section():

    left, right = st.columns(2)

    with left:

        job_file = render_job_upload()

        if job_file:
            st.success(f"Selected: {job_file.name}")

    with right:

        resume_files = render_resume_upload()

        if resume_files:
            st.success(
                f"{len(resume_files)} resume(s) selected."
            )

    st.divider()

    return job_file, resume_files