import os
import shutil

from HowlerMonkey.entity.config_entity import DataSelectorConfig
from HowlerMonkey.utils.common import clear_and_create_folder
from HowlerMonkey import logger


class DataSelector:

        def __init__(self, config: DataSelectorConfig) -> None:
            self.config = config

        def get_equally_spaced_images(self) -> None:
            
            image_files = sorted(os.listdir(self.config.src_images_folder))
            label_files = sorted(os.listdir(self.config.src_labels_folder))
            
            
            # Calculate the step to select N equally spaced images
            step = max(1, len(image_files) // self.config.n_images)
            
            clear_and_create_folder(
                self.config.dest_images_folder,
                self.config.dest_labels_folder
            )

            selected_indices = range(0, len(image_files), step)
            

            for idx in selected_indices:
                image_file = image_files[idx]
                label_file = label_files[idx]
                

                shutil.copy(
                    self.config.src_images_folder / image_file,
                    self.config.dest_images_folder / image_file
                )
                
                shutil.copy(
                      self.config.src_labels_folder / label_file,
                    self.config.dest_labels_folder / label_file
                )

            logger.info(f"Selected {len(selected_indices)} images and labels.")