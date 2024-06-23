import os
import gdown
import shutil
import random
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
                str(zip_download_dir)
            )

            logger.info(f"Downloaded data with id {dataset_id} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)
        os.makedirs(os.path.join(unzip_path, 'images'), exist_ok=True)
        os.makedirs(os.path.join(unzip_path, 'labels'), exist_ok=True)
        

        logger.info(f"Extracting data from {self.config.local_data_file} into {unzip_path}")
        with zipfile.ZipFile(self.config.local_data_file) as zip_file:

            all_images = [file_path for file_path in zip_file.namelist() if file_path.endswith('.png') or file_path.endswith('.jpg')]

            logger.info(f"Filtering {self.config.data_porcentage}% of {len(all_images)} samples")

            num_images = len(all_images)*(self.config.data_porcentage/100)
            filtered_images = random.sample(all_images, int(num_images))
            
            logger.info(f"Extracting {len(filtered_images)} samples")
            for image in filtered_images:

                image_name = os.path.basename(image)
                label_name = image_name.replace('.png', '.txt').replace('.jpg', '.txt')

                image_source = zip_file.open(image)
                label_source = zip_file.open(image.replace('images', 'labels').replace(image_name, label_name))

                image_target = open(os.path.join(unzip_path, 'images', image_name), "wb")
                label_target = open(os.path.join(unzip_path, 'labels', label_name), "wb")
                
                with image_source, image_target:
                    shutil.copyfileobj(image_source, image_target)

                with label_source, label_target:
                    shutil.copyfileobj(label_source, label_target)

            logger.info(f"Extracted {len(all_images)} samples into {unzip_path}")
                