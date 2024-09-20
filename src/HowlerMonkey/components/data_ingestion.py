import glob
import json
import random

from HowlerMonkey.utils.common import copy_images, clear_and_create_folder
from HowlerMonkey.entity.config_entity import DataIngestionConfig
from HowlerMonkey import logger

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def load_fold_file(self):

        logger.info(f"Loading fold file")
        with open(self.config.fold_file, 'r') as f:
            self.folds_info = json.load(f)
        logger.info(f"Fold file loaded")

    def clear_folders(self):
        
        clear_and_create_folder(
            self.config.images_path / 'val', 
            self.config.labels_path / 'val'
        )

        clear_and_create_folder(
            self.config.images_path / 'train', 
            self.config.labels_path / 'train'
        )
        
    def get_images_paths(self):
        logger.info(f"Getting images paths")
        self.images_paths = glob.glob(str(self.config.images_path / 'main' / '*.jpg'))

    def get_assistant_images_paths(self):
        logger.info(f"Getting assistant {self.config.assistant_folder} images paths")
        self.assistant_images_paths = glob.glob(str(self.config.images_path / self.config.assistant_folder / '*.jpg'))

    def merge_assistant_data(self):

        self.get_assistant_images_paths()

        logger.info(f"Select {self.config.n_assistant_images} assistant images")
        
        self.assistant_images_paths = random.sample(
            self.assistant_images_paths, 
            self.config.n_assistant_images
        )

        logger.info(f"Getting train/val proportions")
        
        train_image_prop = 1 / self.config.folds
        train_image_number = int(train_image_prop * self.config.n_assistant_images)
        
        logger.info(f"selectin {train_image_number} to train data")

        train_assistant_images = self.assistant_images_paths[:train_image_number]
        

        copy_images(
            train_assistant_images,
            self.config.labels_path / self.config.assistant_folder, 
            self.config.images_path / "train", 
            self.config.labels_path / "train"
        )

        val_assistant_images = self.assistant_images_paths[train_image_number:]

        copy_images(
            val_assistant_images,
            self.config.labels_path / self.config.assistant_folder, 
            self.config.images_path / "val", 
            self.config.labels_path / "val"
        )



    def split_data(self, fold_id: int):

        self.get_images_paths()

        logger.info(f"Splitting data for fold {fold_id}")

        self.fold_data = next(
            fold for fold in self.folds_info 
                if fold['fold'] == fold_id
        )

        self.train_idx = self.fold_data['train_indices']
        train_images = [self.images_paths[i] for i in self.train_idx]

        copy_images(
            train_images,
            self.config.labels_path / "main", 
            self.config.images_path / "train", 
            self.config.labels_path / "train"
        )



        self.val_idx = self.fold_data['val_indices']
        val_images = [self.images_paths[i] for i in self.val_idx]

        logger.info(f"Copying images to val folder")

        copy_images(
            val_images,
            self.config.labels_path / "main", 
            self.config.images_path / "val", 
            self.config.labels_path / "val"
        )


