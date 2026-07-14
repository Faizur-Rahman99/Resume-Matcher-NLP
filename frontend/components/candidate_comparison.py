import streamlit as st

from utils.demo import display_score


def render_candidate_comparison(results):

    st.header("⚖️ Compare Candidates")

    if len(results) < 2:
        st.info("Upload at least two resumes to compare candidates.")
        return

    filenames = [
        candidate["filename"]
        for candidate in results
    ]

    left, right = st.columns(2)

    with left:
        first = st.selectbox(
            "Candidate 1",
            filenames,
            key="compare1",
        )

    with right:
        second = st.selectbox(
            "Candidate 2",
            filenames,
            index=1,
            key="compare2",
        )

    if first == second:
        st.warning("Please select two different candidates.")
        return

    candidate1 = next(
        c for c in results
        if c["filename"] == first
    )

    candidate2 = next(
        c for c in results
        if c["filename"] == second
    )

    st.divider()

    col1, col2, col3 = st.columns([2, 3, 3])

    col1.markdown("### Metric")
    col2.markdown(f"### {candidate1['filename']}")
    col3.markdown(f"### {candidate2['filename']}")

    metrics = [
        ("Overall Match", "overall_score"),
        ("Skills Match", "skill_score"),
        ("Experience Match", "experience_score"),
    ]

    for title, key in metrics:

        c1, c2, c3 = st.columns([2, 3, 3])

        c1.write(title)

        if key == "overall_score":
            score1 = display_score(candidate1[key])
            score2 = display_score(candidate2[key])
        else:
            score1 = candidate1[key]
            score2 = candidate2[key]

        c2.write(f"{score1:.0%}")
        c3.write(f"{score2:.0%}")

    st.subheader("Matched Skills")

    left, right = st.columns(2)

    with left:
        for skill in candidate1["matched_skills"]:
            st.success(skill)

    with right:
        for skill in candidate2["matched_skills"]:
            st.success(skill)

    st.subheader("Missing Skills")

    left, right = st.columns(2)

    with left:
        for skill in candidate1["missing_skills"]:
            st.error(skill)

    with right:
        for skill in candidate2["missing_skills"]:
            st.error(skill)