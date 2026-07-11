import streamlit as st


def render_job_preview(job_data):

    if not job_data:
        return

    st.success("Job description processed successfully!")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Required Skills")

        for skill in job_data["skills"]:
            st.success(f"📌 {skill}")

    with col2:

        st.subheader("Required Experience")

        st.metric(
            "Years",
            job_data["experience_years"],
        )