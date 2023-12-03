import os
import sys
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent

def get_project_folder() -> Path:

    project_folder_path = os.environ.get('MVGCALC')
    
    return None if project_folder_path is None else Path(project_folder_path)


def get_image_path(relative_path) -> str:
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
