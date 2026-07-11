import streamlit as st
from services.api import APIClient
from components.job_upload import render_job_upload
from components.resume_upload import render_resume_upload
from components.candidate_table import render_candidate_table
from components.candidate_card import render_candidate_cards
from components.header import render_header
from components.upload_section import render_upload_section
from services.analyzer import analyze_candidates
from components.candidate_comparison import render_candidate_comparison

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide",
)

client = APIClient()

render_header()

job_file, resume_files = render_upload_section()


can_analyze = (
    job_file is not None
    and len(resume_files or []) > 0
)

analyze = st.button(
    "🚀 Analyze Candidates",
    type="primary",
    use_container_width=True,
    disabled=not can_analyze,
)

if analyze:

    with st.spinner(
            "Analyzing candidates..."
    ):
        ranking = analyze_candidates(
            job_file,
            resume_files,
        )

        st.success(
            "Candidates ranked successfully!"
        )

        render_candidate_table(
            ranking["results"]
        )

        render_candidate_comparison(
            ranking["results"]
        )

        render_candidate_cards(
            ranking["results"]
        )








