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

            clear_and_create_folder(
                self.config.dest_images_folder,
                self.config.dest_labels_folder
            )

            logger.info(f"Selecing {self.config.n_images} images and labels.")

            selected_indices = [
                int(round(i * (len(image_files) - 1) / (self.config.n_images - 1)))
                for i in range(self.config.n_images)
            ]

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