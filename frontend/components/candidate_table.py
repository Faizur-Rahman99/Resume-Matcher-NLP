import streamlit as st


def render_candidate_table(results):

    st.header("🏆 Candidate Rankings")

    medals = [
        "🥇",
        "🥈",
        "🥉",
    ]

    for index, candidate in enumerate(results):

        medal = (
            medals[index]
            if index < 3
            else "📄"
        )

        score = candidate["overall_score"]

        with st.container(border=True):

            left, right = st.columns([5, 1])

            with left:

                st.subheader(
                    f"{medal} {candidate['filename']}"
                )

            with right:

                st.metric(
                    "Match",
                    f"{score:.1%}",
                )

            st.progress(score)