import streamlit as st

from utils.demo import (
    display_score,
    match_level,
)

def render_candidate_table(results):
    """
    Render the ranked candidate overview.
    """

    st.header("🏆 Candidate Rankings")

    if not results:
        st.warning("No candidates to display.")
        return

    # ---------- Dashboard Summary ----------

    total_candidates = len(results)

    average_score = (
            sum(
                candidate["overall_score"]
                for candidate in results
            )
            / total_candidates
    )

    average_score = display_score(
        average_score
    )

    best_candidate = results[0]
    best_score = display_score(
        best_candidate["overall_score"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Candidates",
        total_candidates,
    )

    col2.metric(
        "📈 Average Match",
        f"{average_score:.1%}",
    )

    col3.metric(
        "🥇 Best Match",
        f"{best_score:.1%}",
    )

    col4.metric(
        "📄 Top Resume",
        best_candidate["filename"],
    )

    st.divider()

    medals = [
        "🥇",
        "🥈",
        "🥉",
    ]

    for index, candidate in enumerate(results):

        medal = (
            medals[index]
            if index < 3
            else f"#{index + 1}"
        )

        score = display_score(
            candidate["overall_score"]
        )

        color = match_level(score)

        with st.container(border=True):

            left, middle, right = st.columns([5, 2, 2])

            with left:

                st.subheader(
                    f"{medal} {candidate['filename']}"
                )

                st.caption(color)

            with middle:

                st.metric(
                    "Overall Match",
                    f"{score:.1%}",
                )

            with right:

                st.metric(
                    "Matched Skills",
                    len(candidate.get("matched_skills", [])),
                )

            st.progress(score)