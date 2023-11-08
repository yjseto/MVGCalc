from PyQt5.QtWidgets import QApplication
from gui.util.css import build_css_string

from lib.models.user_input import UserInput
from lib.enums.modes import DisplayMode

class MvgCalcApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.user_input = UserInput()
        self.display_mode = DisplayMode.BASIC #default to BASIC
        self.h_pos = None
        
        self.setStyleSheet(build_css_string(
        "QWidget",
        background_color = "#161A20",
        font_family = "roboto", 
        font_size = "28px",
        color = "white"
    ))