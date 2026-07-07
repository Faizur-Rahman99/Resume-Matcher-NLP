from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    raw_data_dir: Path = Path("data/raw")


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Downloads or copies datasets into the raw data directory.
        """
        pass
    