from PyQt5.QtWidgets import QApplication

from lib.models.user_input import UserInput
from lib.enums.modes import DisplayMode

class MvgCalcApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.user_input = UserInput()
        self.display_mode = DisplayMode.BASIC #default to BASIC