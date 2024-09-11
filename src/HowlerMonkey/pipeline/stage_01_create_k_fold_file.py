from HowlerMonkey.config.configuration import ConfigurationManager
from HowlerMonkey.components.k_fold_creator import KFoldCreator
from HowlerMonkey import logger

STAGE_NAME = "Create KFold file"


class KFoldCreationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        kfold_creator = KFoldCreator(config.get_kfold_config())
        kfold_creator.create_folder()
        kfold_creator.get_images_paths()
        kfold_creator.create_kfolds()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = KFoldCreationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e