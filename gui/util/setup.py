    
from lib.enums.constants import WINDOW_HEIGHT, WINDOW_WIDTH

height_input_multiplier =0.0772
width_input_multiplier = 0.1739

width_nav_multiplier = 0.2915
height_nav_multiplier = 0.04830

def get_input_button_height():
    return height_input_multiplier * WINDOW_HEIGHT
def get_input_button_width():
    return width_input_multiplier * WINDOW_WIDTH

def get_nav_button_height():
    return height_nav_multiplier * WINDOW_HEIGHT
def get_nav_button_width():
    return width_nav_multiplier * WINDOW_WIDTH