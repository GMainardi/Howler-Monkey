import torch
from pathlib import Path
from ultralytics import YOLO

from src.HowlerMonkey.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_model(self):
        self.model = YOLO(self.config.model_path)
    

    def train(self):

        self.model.train(
            data=self.config.data_file_path,
            epochs=self.config.params_epochs,
            batch=self.config.params_batch_size,
            project=self.config.root_dir
        )
