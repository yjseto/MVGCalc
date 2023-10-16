from PyQt5.QtWidgets import QApplication
from lib.models.user_input import UserInput

class MvgCalcApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.user_input = UserInput()