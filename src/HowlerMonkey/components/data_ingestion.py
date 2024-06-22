import os
import gdown
import shutil
import zipfile



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
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        os.makedirs(os.path.join(unzip_path, 'images'), exist_ok=True)
        os.makedirs(os.path.join(unzip_path, 'labels'), exist_ok=True)
        

        with zipfile.ZipFile(self.config.local_data_file) as zip_file:
            for member in zip_file.namelist():
                filename = os.path.basename(member)
                # skip directories
                if not filename:
                    continue
            
                # copy file (taken from zipfile's extract)
                source = zip_file.open(member)
                if filename.endswith('.png') or filename.endswith('.jpg'):
                    target = open(os.path.join(unzip_path, 'images', filename), "wb")
                elif filename.endswith('.txt'):
                    target = open(os.path.join(unzip_path, 'labels', filename), "wb")
                else:
                    continue
                
                with source, target:
                    shutil.copyfileobj(source, target)