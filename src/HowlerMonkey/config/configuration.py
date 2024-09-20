from HowlerMonkey.constants import *
from HowlerMonkey.utils.common import read_yaml, create_directories

from HowlerMonkey.entity.config_entity import KFoldConfig
from HowlerMonkey.entity.config_entity import DataSelectorConfig
from HowlerMonkey.entity.config_entity import DataIngestionConfig
from HowlerMonkey.entity.config_entity import TrainingConfig


class ConfigurationManager:
    
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_kfold_config(self) -> KFoldConfig:

        config = self.config.kfold

        create_directories([config.root_dir])
        
        data_ingestion_config = KFoldConfig(
            root_dir=Path(config.root_dir),
            seed=config.seed,
            folds=config.folds,
            fold_file=Path(config.root_dir) / config.fold_file,
            images_path=Path(config.images_path)
        )
        
        
        return data_ingestion_config
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        kfold_config = self.config.kfold

        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir        = Path(config.root_dir),
            n_assistant_images = config.n_assistant_images,
            assistant_folder = Path(config.assistant_folder),
            fold_file= Path(kfold_config.root_dir) / kfold_config.fold_file,
            images_path = Path(kfold_config.images_path),
            labels_path= Path(kfold_config.labels_path),
            folds = kfold_config.folds
        )
        
        
        return data_ingestion_config
    
    def get_training_config(self):

        training = self.config.training

        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir = Path(training.root_dir),
            model_path = training.model_path,
            data_file_path = Path(training.data_file_path),
            params_epochs = self.params.EPOCHS,
            params_batch_size = self.params.BATCH_SIZE,
            model_name= training.model_name
        )
        
        return training_config
    


    def get_data_selector_config(self) -> DataSelectorConfig:

        config = self.config.data_selector
        kfconfig = self.config.kfold
        
        data_ingestion_config = DataSelectorConfig(
            src_images_folder= Path(kfconfig.images_path) / Path(config.src_folder_name),
            src_labels_folder= Path(kfconfig.labels_path) / Path(config.src_folder_name),
            dest_images_folder= Path(kfconfig.images_path) / Path(config.dest_folder_name),
            dest_labels_folder= Path(kfconfig.labels_path) / Path(config.dest_folder_name),
            n_images = int(config.n_images)
        )
        
        
        return data_ingestion_config