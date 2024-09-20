from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class KFoldConfig:
    root_dir: Path
    seed: int
    folds: int
    fold_file: Path
    images_path: Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    n_assistant_images: int
    assistant_folder: Path
    fold_file: Path
    images_path: Path
    labels_path: Path
    folds: int


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    model_path: str
    data_file_path: Path
    params_epochs: int
    params_batch_size: int
    model_name: str

@dataclass(frozen=True)
class DataSelectorConfig:
    src_images_folder: Path
    src_labels_folder: Path
    dest_images_folder: Path
    dest_labels_folder: Path
    n_images: int
    