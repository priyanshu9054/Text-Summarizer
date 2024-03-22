import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file and returns
    
    Args: 
        path_to_yaml (Path): Path to yaml file
    
    Raises:
        BoxValueError: Raised when yaml file is not found or yaml is empty
    
    Returns:
    
    ConfigBox: Returns ConfigBox object
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dictionaries: list, verbose=True):
    """
    Create directories for the given path_to_dictionaries
    
    Args:
        path_to_dictionaries (list): List of paths to dictionaries
        verbose (bool, optional): If True, print information. Defaults to True.
    
    Raises:
        BoxValueError: Raised when any of the given path_to_dictionaries is not a directory
    
    Returns:
    
    """
    for path in path_to_dictionaries:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path} ")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size of a file in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"