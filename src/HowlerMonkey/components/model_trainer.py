from ultralytics import YOLO

from HowlerMonkey.entity.config_entity import TrainingConfig
from HowlerMonkey import logger


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_model(self):
        logger.info(f"Loading model")
        self.model = YOLO(self.config.model_path)

    def train(self):
        
        logger.info(f"Training model")
        self.model.train(
            data=self.config.data_file_path,
            epochs=self.config.params_epochs,
            batch=self.config.params_batch_size,
            project=self.config.model_name,
            device=self.config.device,
            patience=50,
        )

        logger.info(f"Model trained")


    def eval(self):

        logger.info(f"Eval model")

        self.model.val(
            split = 'test'
        )