from enum import Enum
from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import  QHBoxLayout

from gui.components.button import MvgCalcNavButton
from gui.util.css import *
from PyQt5 import QtGui

class NavBar(QHBoxLayout):

    clicked_display_signal = pyqtSignal(Enum)

    def __init__(self, *args : Enum):
        super().__init__()

        for arg  in args:
            button = MvgCalcNavButton(arg.textSymbol)
            if arg.iconPath is not None:
                button.setIcon(QtGui.QIcon(arg.iconPath))
            button.setStyleSheet(component_pale_gray("QPushButton"))
            button.clicked.connect(partial(self.handle_button_click, arg))
            self.addWidget(button)
            


            
    def handle_button_click(self, display_mode : Enum):

        self.clicked_display_signal.emit(display_mode)
        
    