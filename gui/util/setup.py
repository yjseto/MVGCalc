    
from lib.util.constants import WINDOW_HEIGHT, WINDOW_WIDTH
from lib.util.utils import get_project_root

#height/width multiplier
width_input_multiplier = 0.1739
height_input_multiplier =0.0772

width_nav_multiplier = 0.2915
height_nav_multiplier = 0.04830

width_function_multiplier = 0.20716
height_function_multiplier = 0.07850

def get_input_button_height():
    return height_input_multiplier * WINDOW_HEIGHT
def get_input_button_width():
    return width_input_multiplier * WINDOW_WIDTH

def get_nav_button_height():
    return height_nav_multiplier * WINDOW_HEIGHT
def get_nav_button_width():
    return width_nav_multiplier * WINDOW_WIDTH

#Image Paths
HISTORIC_EXPRESSION_ICON_FILE_PATH = f"{get_project_root()}\\gui\\images\\history.png"

#Directional Arrows
D_PAD_UP_ICON_FILE_PATH = f"{get_project_root()}\\gui\\images\\up_arrow.png"
D_PAD_DOWN_ICON_FILE_PATH = f"{get_project_root()}\\gui\\images\\down_arrow.png"
D_PAD_LEFT_ICON_FILE_PATH = f"{get_project_root()}\\gui\\images\\left_arrow.png"
D_PAD_RIGHT_ICON_FILE_PATH = f"{get_project_root()}\\gui\\images\\right_arrow.png"

