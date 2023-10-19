from PyQt5.QtWidgets import QApplication
from lib.models.user_input import UserInput
#from gui.components.graph_display import GraphDisplay

class MvgCalcApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.user_input = UserInput()
        #self.graph_display = GraphDisplay(self.user_input)