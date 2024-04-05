import os


from src.HowlerMonkey.constants import *
from src.HowlerMonkey.utils.common import read_yaml, create_directories


from src.HowlerMonkey.entity.config_entity import DataIngestionConfig
from src.HowlerMonkey.entity.config_entity import TrainingConfig
from src.HowlerMonkey.entity.config_entity import EvaluationConfig
from src.HowlerMonkey.entity.config_entity import PredictionConfig

class ConfigurationManager:

    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir        = config.root_dir,
            data_id         = config.data_id,
            local_data_file = config.local_data_file,
            unzip_dir       = config.unzip_dir 
        )
        
        
        return data_ingestion_config
    
    def get_training_config(self):

        training = self.config.training

        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir          = Path(training.root_dir),
            model_path        = training.model_path,
            data_file_path    = Path(training.data_file_path),
            params_epochs     = self.params.EPOCHS,
            params_batch_size = self.params.BATCH_SIZE
        )
        
        return training_config
    

    def get_evaluation_config(self) -> EvaluationConfig:

        evaluation_config = EvaluationConfig(
            model_path = self.config.training.root_dir,
            data_path  = self.config.training.data_file_path,
            all_params = self.params,
            mlflow_uri = os.environ["MLFLOW_TRACKING_URI"],
            model_name = self.config.training.model_path.split('/')[-1].split('.')[0]
        )
        return evaluation_config
    

    def get_prediction_config(self):

        predicting = self.config.predicting

        create_directories([
            Path(predicting.root_dir)
        ])
                
        prediction_config = PredictionConfig(
            root_dir          = Path(predicting.root_dir),
            model_path        = self.config.training.root_dir,
            prediction_output = predicting.prediction_output
        )

        return prediction_config