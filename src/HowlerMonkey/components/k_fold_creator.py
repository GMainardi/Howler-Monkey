import json
import glob
import numpy as np
from sklearn.model_selection import KFold

from HowlerMonkey import logger
from HowlerMonkey.entity.config_entity import KFoldConfig

class KFoldCreator:

    def __init__(self, config: KFoldConfig):
        self.config = config

    def create_folder(self):
        logger.info(f"Creating KFold folder at {self.config.root_dir}")

        self.kf = KFold(n_splits=self.config.folds, shuffle=True, random_state=self.config.seed)

    def get_images_paths(self):
        logger.info(f"Getting images paths from {self.config.images_path}")
        self.images_paths = glob.glob(str(self.config.images_path/ 'main' / '*.jpg'))

    def create_kfolds(self):
        
        self.folds_info = []

        logger.info(f"Creating {self.config.folds}")

        for fold, (train_idx, val_idx) in enumerate(self.kf.split(self.images_paths)):
            
            fold_data = {
                'fold': fold,
                'train_indices': train_idx.tolist(),
                'val_indices': val_idx.tolist()
            }
            self.folds_info.append(fold_data)

        logger.info(f"KFold created")
        logger.info(f"Saving KFold info at {self.config.fold_file}")

        with open(self.config.fold_file, 'w') as f:
            json.dump(self.folds_info, f, indent=4)

        logger.info(f"KFold info saved")

            

            