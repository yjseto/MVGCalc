from PyQt5.QtWidgets import QPushButton
from lib.util.constants import WINDOW_HEIGHT, WINDOW_WIDTH

from gui.util.setup import (
                        get_input_button_width, 
                        get_input_button_height, 
                        get_nav_button_width, 
                        get_nav_button_height
                    )
        
    
class MvgCalcInputButton(QPushButton):
    def __init__(self, text: str, parent = None):
        super().__init__(text, parent)
        self.setFixedSize(int(get_input_button_width()),int(get_input_button_height()))
        
class MvgCalcHalfInputButton(QPushButton):
    def __init__(self, text: str, width: int, height: int, parent = None):
        super().__init__(text, parent)
        self.setFixedSize(int(width*WINDOW_WIDTH),int(height * WINDOW_HEIGHT))
        
class MvgCalcInputButton2(QPushButton):
    def __init__(self, text: str, width: int, height: int, parent = None):
        super().__init__(text, parent)
        self.setFixedSize(int(width*WINDOW_WIDTH),int(height * WINDOW_HEIGHT))

class MvgCalcNavButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(int(get_nav_button_width()),int(get_nav_button_height()))

         
          
            
