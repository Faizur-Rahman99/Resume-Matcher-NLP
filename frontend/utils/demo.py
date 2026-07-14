import os


def demo_mode() -> bool:
    return (
        os.getenv(
            "USE_SEMANTIC",
            "true",
        ).lower() == "false"
    )


def display_score(score: float) -> float:
    """
    Calibrate displayed scores in demo mode.
    Backend ranking is unchanged.
    """
    if demo_mode():
        return min(score * 1.06, 1.0)

    return score


def match_level(score: float) -> str:
    """
    Return the match label based on the displayed score.
    """

    if demo_mode():

        if score >= 0.80:
            return "🟢 Excellent"

        elif score >= 0.65:
            return "🟡 Good"

        elif score >= 0.45:
            return "🟠 Fair"

        return "🔴 Weak"

    if score >= 0.85:
        return "🟢 Excellent"

    elif score >= 0.70:
        return "🟡 Good"

    elif score >= 0.50:
        return "🟠 Fair"

    return "🔴 Weak"