from ultralytics import settings


from HowlerMonkey.pipeline.stage_00_data_selector import DataSelectorPipeline
from HowlerMonkey.pipeline.stage_01_create_k_fold_file import KFoldCreationPipeline
from HowlerMonkey.pipeline.stage_02_training import ModelTrainingPipeline
from HowlerMonkey import logger


STAGE_NAME = "Create KFold file"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = DataSelectorPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e

STAGE_NAME = "Create KFold file"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   obj = KFoldCreationPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model training"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = ModelTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e