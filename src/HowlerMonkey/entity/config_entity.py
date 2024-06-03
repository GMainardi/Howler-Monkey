from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    data_id: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    model_path: str
    data_file_path: Path
    params_epochs: int
    params_batch_size: int
    params_image_size: int

@dataclass(frozen=True)
class EvaluationConfig:
    model_path: Path
    data_path: Path
    all_params: dict
    mlflow_uri: str
    model_name: str


@dataclass(frozen=True)
class PredictionConfig:
    root_dir: Path
    model_path: Path
    prediction_output: Path