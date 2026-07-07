from src.batch.resume_loader import ResumeLoader
from src.entity.job_description import JobDescription
from src.io.document_processor import DocumentProcessor
from src.matching.similarity_engine import SimilarityEngine


class BatchProcessor:

    def __init__(self):
        self.loader = ResumeLoader()
        self.processor = DocumentProcessor()
        self.engine = SimilarityEngine()

    def process(
        self,
        folder: str,
        job: JobDescription,
    ):

        results = []

        for path in self.loader.load(folder):

            resume = self.processor.process(str(path))

            match = self.engine.match(
                resume,
                job,
            )

            results.append(
                {
                    "filename": path.name,
                    "resume": resume,
                    "match": match,
                }
            )

        results.sort(
            key=lambda item: item["match"].overall_score,
            reverse=True,
        )

        return results