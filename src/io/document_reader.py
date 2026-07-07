from pathlib import Path

from src.io.docx_reader import DOCXReader
from src.io.pdf_reader import PDFReader
from src.io.text_reader import TextReader


class DocumentReader:

    def __init__(self):
        self.pdf_reader = PDFReader()
        self.docx_reader = DOCXReader()
        self.text_reader = TextReader()

    def read(self, path: str) -> str:

        extension = Path(path).suffix.lower()

        if extension == ".txt":
            return self.text_reader.read(path)

        if extension == ".pdf":
            return self.pdf_reader.read(path)

        if extension == ".docx":
            return self.docx_reader.read(path)

        raise ValueError(
            f"Unsupported file format: {extension}"
        )