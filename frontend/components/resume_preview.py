import streamlit as st


def render_resume_preview(resume_data):

    if not resume_data:
        return

    st.success("Resume processed successfully!")

    # ---------- Personal Information ----------

    st.subheader("👤 Candidate Information")

    st.write(f"**Name:** {resume_data['name']}")
    st.write(f"**Email:** {resume_data['email']}")
    st.write(f"**Phone:** {resume_data['phone']}")

    st.divider()

    # ---------- Skills & Experience ----------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Extracted Skills")

        for skill in resume_data["skills"]:
            st.success(f"✅ {skill}")

    with col2:

        st.subheader("Experience")

        st.metric(
            "Years",
            resume_data["experience_years"],
        )

    st.divider()

    # ---------- Education ----------

    st.subheader("🎓 Education")

    if resume_data["education"]:

        for degree in resume_data["education"]:
            st.write(f"• {degree}")

    else:

        st.info("No education found.")