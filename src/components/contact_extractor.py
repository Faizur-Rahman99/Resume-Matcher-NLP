import re


class ContactExtractor:

    EMAIL_PATTERN = (
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    PHONE_PATTERN = (
        r"(?:\+?\d{1,3}[- ]?)?(?:\(?\d{2,4}\)?[- ]?)?\d{3,5}[- ]?\d{3,5}"
    )

    def extract_email(self, text: str):

        match = re.search(
            self.EMAIL_PATTERN,
            text,
        )

        if match:
            return match.group()

        return None

    def extract_phone(self, text: str):

        match = re.search(
            self.PHONE_PATTERN,
            text,
        )

        if match:
            return match.group()

        return None