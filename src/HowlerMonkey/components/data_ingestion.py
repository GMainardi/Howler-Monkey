import os
import zipfile
import gdown


from HowlerMonkey import logger
from HowlerMonkey.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_id = self.config.data_id
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Downloading data with id {dataset_id} into file {zip_download_dir}")

            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(
                prefix+dataset_id,
                zip_download_dir
            )

            logger.info(f"Downloaded data with id {dataset_id} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)