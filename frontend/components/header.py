import streamlit as st


def render_header():
    """
    Render the application header.
    """

    st.title("🤖 AI Resume Matcher")

    st.markdown(
        """
        **AI-powered Resume Ranking using NLP and Sentence Transformers**

        Upload a job description and multiple resumes to automatically
        identify the strongest candidates based on semantic similarity,
        skills, education, and experience.
        """
    )

    st.info(
        "📄 Supported formats: **PDF, DOCX, TXT** | "
        "📤 Upload **1 Job Description** + **Multiple Resumes**"
    )

    st.divider()