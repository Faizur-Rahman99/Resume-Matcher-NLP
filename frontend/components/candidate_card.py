import streamlit as st


def render_candidate_cards(results):

    st.subheader("📋 Candidate Details")

    for index, candidate in enumerate(results):

        if index == 0:
            rank = "🥇"
            st.success("🏆 Top Ranked Candidate")
        elif index == 1:
            rank = "🥈"
        elif index == 2:
            rank = "🥉"
        else:
            rank = f"#{index + 1}"

        score = candidate.get("overall_score", 0)

        if score >= 0.85:
            level = "🟢 Excellent Match"
        elif score >= 0.70:
            level = "🟡 Good Match"
        elif score >= 0.50:
            level = "🟠 Fair Match"
        else:
            level = "🔴 Weak Match"

        with st.expander(
                f"{rank} {candidate.get('filename', 'Unknown')} • "
                f"{candidate.get('overall_score', 0):.0%} Match • {level}"
        ):

            # ---------- Candidate Information ----------

            st.subheader("👤 Candidate Information")

            left, right = st.columns(2)

            with left:
                st.write(f"**👤 Name:** {candidate.get('name') or 'Not found'}")
                st.write(f"**📧 Email:** {candidate.get('email') or 'Not found'}")

            with right:
                st.write(f"**📱 Phone:** {candidate.get('phone') or 'Not found'}")

            st.divider()

            # ---------- Education ----------

            st.subheader("🎓 Education")

            education = candidate.get(
                "education",
                [],
            )

            if education:

                for degree in education:
                    st.write(f"• {degree}")

            else:

                st.info("No education found.")

            st.divider()

            # ---------- Projects ----------

            st.subheader("📂 Projects")

            projects = candidate.get(
                "projects",
                [],
            )

            if projects:

                for project in projects:
                    st.write(f"• {project}")

            else:

                st.info("No projects found.")

            st.divider()

            # ---------- Match Scores ----------

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Overall Match",
                    f"{candidate.get('overall_score', 0):.0%}",
                )

                st.progress(
                    candidate.get(
                        "overall_score",
                        0.0,
                    )
                )

                st.metric(
                    "Skills Match",
                    f"{candidate.get('skill_score', 0):.0%}",
                )

                st.progress(
                    candidate.get(
                        "skill_score",
                        0.0,
                    )
                )

                st.metric(
                    "Experience Match",
                    f"{candidate.get('experience_score', 0):.0%}",
                )

                st.progress(
                    candidate.get(
                        "experience_score",
                        0.0,
                    )
                )

            with col2:

                # ---------- Matched Skills ----------

                st.subheader("✅ Matched Skills")

                matched_skills = candidate.get(
                    "matched_skills",
                    [],
                )

                if matched_skills:

                    st.markdown(
                        " ".join(
                            f"`{skill}`"
                            for skill in matched_skills
                        )
                    )

                else:

                    st.info("No matched skills")

                # ---------- Missing Skills ----------

                st.subheader("❌ Missing Skills")

                missing_skills = candidate.get(
                    "missing_skills",
                    [],
                )

                if missing_skills:

                    st.markdown(
                        " ".join(
                            f"`{skill}`"
                            for skill in missing_skills
                        )
                    )

                else:

                    st.success("No missing skills")

            st.divider()

            # ---------- Match Explanation ----------

            st.subheader("💡 Match Explanation")

            explanation = candidate.get(
                "explanation",
                [],
            )

            if explanation:

                for item in explanation:
                    st.markdown(f"- {item}")
            else:

                st.info("No explanation available.")