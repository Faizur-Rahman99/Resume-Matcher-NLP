from docx import Document


class DOCXReader:

    def read(self, path: str) -> str:

        document = Document(path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )