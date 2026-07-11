import streamlit as st


def render_resume_preview(resume_data):

    if not resume_data:
        return

    st.success("Resume processed successfully!")

    # ---------- Personal Information ----------

    st.subheader("👤 Candidate Information")

    st.write(f"**Name:** {resume_data.get('name') or 'Not found'}")
    st.write(f"**Email:** {resume_data.get('email') or 'Not found'}")
    st.write(f"**Phone:** {resume_data.get('phone') or 'Not found'}")

    st.divider()

    # ---------- Skills & Experience ----------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💻 Extracted Skills")

        skills = resume_data.get("skills", [])

        if skills:
            for skill in skills:
                st.success(f"✅ {skill}")
        else:
            st.info("No skills found.")

    with col2:

        st.subheader("📅 Experience")

        st.metric(
            "Years",
            resume_data.get("experience_years", 0),
        )

    st.divider()

    # ---------- Education ----------

    st.subheader("🎓 Education")

    education = resume_data.get("education", [])

    if education:

        for degree in education:
            st.write(f"• {degree}")

    else:

        st.info("No education found.")

    st.divider()

    # ---------- Projects ----------

    st.subheader("📂 Projects")

    projects = resume_data.get("projects", [])

    if projects:

        for project in projects:
            st.write(f"• {project}")

    else:

        st.info("No projects found.")