from HowlerMonkey.config.configuration import ConfigurationManager
from HowlerMonkey.components.data_selector import DataSelector
from HowlerMonkey import logger

STAGE_NAME = "Create KFold file"


class DataSelectorPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_selector = DataSelector(config.get_data_selector_config())
        data_selector.get_equally_spaced_images()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataSelectorPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e