from src.components.resume_parser import ResumeParser
from src.io.document_reader import DocumentReader


class DocumentProcessor:

    def __init__(self):
        self.reader = DocumentReader()
        self.parser = ResumeParser()

    def process(self, path: str):

        text = self.reader.read(path)

        return self.parser.parse(text)




