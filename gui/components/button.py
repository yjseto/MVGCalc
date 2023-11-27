from PyQt5.QtWidgets import QPushButton
from gui.enums.styles import COLORS
from gui.util.css import build_css_string, component_pale_gray
from lib.util.constants import WINDOW_HEIGHT, WINDOW_WIDTH
        
        
class MvgCalcInputButton(QPushButton):
    def __init__(self, text: str, width: int, height: int, parent = None):
        super().__init__(text, parent)
        self.setFixedSize(int(width * WINDOW_WIDTH),int(height * WINDOW_HEIGHT))

class MvgCalcNavButton(MvgCalcInputButton):
    def __init__(self, text: str,  width: int, height: int, parent = None):
        super().__init__(text, width, height, parent)

        #give nav button the same behavior as a checkbox
        self.setCheckable(True)
        self.clicked.connect(self.set_pressed)
        self.setStyleSheet(component_pale_gray("QPushButton"))

    def set_pressed(self):
        if self.isChecked():
            self.setStyleSheet(
                build_css_string(
                    "QPushButton",
                    background_color= COLORS.BLUE.value, 
                    color=COLORS.WHITE.value, 
                    border_radius="15px",
                    font_size = "17px"
                )
            )
    
    def remove_pressed(self):
        self.setChecked(False)
        self.setStyleSheet(component_pale_gray("QPushButton"))
         
          
            
