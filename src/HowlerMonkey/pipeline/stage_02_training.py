from HowlerMonkey.config.configuration import ConfigurationManager
from HowlerMonkey.components.data_ingestion import DataIngestion
from HowlerMonkey.components.model_trainer import Training
from HowlerMonkey import logger

STAGE_NAME = "Data ingestion"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestor = DataIngestion(config.get_data_ingestion_config())
        data_ingestor.load_fold_file()

        trainer = Training(config.get_training_config())
        trainer.get_model()

        for i in range(config.config.kfold.folds):

            for _ in range(1):
                data_ingestor.clear_folders()

                data_ingestor.split_data(fold_id=i)
                data_ingestor.merge_assistant_data()
                
                trainer.get_model()
                trainer.train()
                trainer.eval()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e