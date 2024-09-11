import os
import yaml
import json
import base64
import shutil
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError

from HowlerMonkey import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns

    Args:
        path_to_yaml (Path): Path to yaml file

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox object
    """
    
    try:

        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError('empty file') from e
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of directories
        verbose (bool, optional): [description]. Defaults to True.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")

@ensure_annotations
def save_json(path: str, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json data
    
    Args:
        path (Path): Path to load json data
    
    Returns:
        ConfigBox: json data
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f'json file loaded from: {path}')
    return ConfigBox(data)


@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Save binary data
    
    Args:
        path (Path): Path to save binary data
        data (Any): binary data
    """
    joblib.dump(value=data, filename=path)
    logger.info(f'binary file saved at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data
    
    Args:
        path (Path): Path to load binary data
    
    Returns:
        Any: binary data
    """
    data = joblib.load(path)
    logger.info(f'binary file loaded from: {path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB
    
    Args:
        path (Path): Path to file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"_ {size_in_kb} KB"

@ensure_annotations
def decode_image(imgstring: str, filename: str):
    """
    Decode image string and save it to filename

    Args:
        imgstring (str): image string
        filename (str): filename

    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)

    logger.info(f'Image saved at: {filename}')


@ensure_annotations
def encode_image_into_base64(croppedImagePath: Path) -> str:
    """
    Encode image into base64

    Args:
        croppedImagePath (Path): Path to image

    Returns:
        str: image string
    """
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())


def get_latest_model(root_path: Path):

    directories = [os.path.join(root_path, d) for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]

    latest_directory = sorted(directories, key=os.path.getmtime, reverse=True)[0]

    return os.path.join(latest_directory, 'weights', 'best.pt')


def clean_scores(scores: dict) -> dict:
    new_scores = {}
    for key, value in scores.items():
        if 'metrics' in key:
            new_key = ''.join([char for char in key if char.isalnum()])
            new_scores[new_key] = value
    return new_scores

def copy_images(images, labels_folder, dest_image_folder, dest_label_folder):
    logger.info(f"Copying images to {dest_image_folder} folder")
    
    for img_path in images:
        img_name = os.path.basename(img_path)
        label_name = img_name.replace('.jpg', '.txt')

        shutil.copy(img_path, dest_image_folder / img_name)
        shutil.copy(labels_folder / label_name, dest_label_folder / label_name)

def clear_and_create_folder(image_folder, label_folder):
    logger.info(f"Clearing {image_folder.name} folder")

    if os.path.exists(image_folder):
        shutil.rmtree(image_folder)
    if os.path.exists(label_folder):
        shutil.rmtree(label_folder)

    logger.info(f"Creating {image_folder.name} folder")
    os.makedirs(image_folder)
    os.makedirs(label_folder)