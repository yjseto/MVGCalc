from decimal import ROUND_DOWN
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton
from lib.enums.constants import *
from gui.util.setup import *
class MvgCalcButton(QPushButton):

    button_click_signal = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(text, parent) 

        #attach click listener to button click event
        self.clicked.connect(self.handle_button_click)


    #transmit signal to the parent component to indicate button has been clicked
    def handle_button_click(self):
        self.button_click_signal.emit()
        
    
class MvgCalcInputButton(MvgCalcButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(int(get_input_button_width()),int(get_input_button_height()))
        
class MvgCalcHalfInputButton(MvgCalcButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(int(get_input_button_width()*0.5),int(get_input_button_height()))

class MvgCalcNavButton(MvgCalcButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(int(get_nav_button_width()),int(get_nav_button_height()))
         
          
            
