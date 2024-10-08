import shutil


from HowlerMonkey.config.configuration import ConfigurationManager
from HowlerMonkey.components.data_ingestion import DataIngestion
from HowlerMonkey import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        
        shutil.rmtree(config.config.data_ingestion.root_dir, ignore_errors=True)
        
        train_data1_ingestion_config = config.get_train1_data_ingestion_config()
        traning_data_ingestion = DataIngestion(train_data1_ingestion_config)
        traning_data_ingestion.download_file()
        traning_data_ingestion.extract_zip_file()

        train_data2_ingestion_config = config.get_train2_data_ingestion_config()
        traning_data_ingestion = DataIngestion(train_data2_ingestion_config)
        traning_data_ingestion.download_file()
        traning_data_ingestion.extract_zip_file()

        val_data_ingestion_config = config.get_val_data_ingestion_config()
        val_data_ingestion = DataIngestion(val_data_ingestion_config)
        val_data_ingestion.download_file()
        val_data_ingestion.extract_zip_file()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e