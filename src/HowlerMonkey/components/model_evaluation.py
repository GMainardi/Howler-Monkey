import pathlib as Path
import mlflow
import mlflow.pytorch
from ultralytics import YOLO
from urllib.parse import urlparse

from src.HowlerMonkey.utils.common import save_json, get_latest_model, clean_scores
from src.HowlerMonkey.entity.config_entity import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    @staticmethod
    def load_model(model_path: Path):
        return YOLO(get_latest_model(model_path))


    def evaluation(self):

        self.model = self.load_model(self.config.model_path)
        self.score = self.model.val(data=self.config.data_path).results_dict
        self.save_score()

    def save_score(self):
        self.scores = clean_scores(self.score)
        save_json(path="scores.json", data=self.scores)

    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                self.scores
            )
            # Model registry does not work with file store
            mlflow.log_artifact(get_latest_model(self.config.model_path), "model")