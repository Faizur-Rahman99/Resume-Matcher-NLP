import re

from src.constants.technical_terms import TECHNICAL_TERMS


class TechnicalTermProtector:
    """
    Protects technical terms during preprocessing by replacing
    them with placeholders and restoring them later.
    """

    @staticmethod
    def protect(text: str):
        """
        Replace technical terms with placeholders.

        Returns
        -------
        tuple[str, dict]
            Protected text and placeholder mapping.
        """

        mapping = {}

        for index, term in enumerate(TECHNICAL_TERMS):

            placeholder = f"__TECH_{index}__"

            pattern = re.compile(
                re.escape(term),
                flags=re.IGNORECASE
            )

            if pattern.search(text):

                text = pattern.sub(placeholder, text)

                mapping[placeholder] = term.lower()

        return text, mapping

    @staticmethod
    def restore(text: str, mapping: dict):

        for placeholder, term in mapping.items():

            text = text.replace(placeholder.lower(), term)
            text = text.replace(placeholder, term)

        return text