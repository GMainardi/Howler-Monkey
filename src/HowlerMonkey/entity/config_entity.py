from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_id: str
    local_data_file: Path
    unzip_dir: Path