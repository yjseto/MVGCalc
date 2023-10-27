from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton, QWidget

from typing import Optional

from lib.models.user_input import UserInput

class MvgCalcButton(QPushButton):

    button_click_signal = pyqtSignal()

    def __init__(self, text, parent=None):
        super().__init__(text, parent) 

        #attach click listener to button click event
        self.clicked.connect(self.handle_button_click)


    #transmit signal to the parent component to indicate button has been clicked
    def handle_button_click(self):
        self.button_click_signal.emit()
          
            
