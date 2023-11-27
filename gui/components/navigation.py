from enum import Enum
from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import  QHBoxLayout

from gui.components.button import MvgCalcNavButton
from gui.util.css import *
from gui.util.setup import width_nav_multiplier, height_nav_multiplier
from PyQt5 import QtGui
from lib.enums.base import IconEnum

class NavBar(QHBoxLayout):

    clicked_display_signal = pyqtSignal(Enum)

    def __init__(self, *args : IconEnum):
        super().__init__()

        for arg  in args:
            button = MvgCalcNavButton(arg.textSymbol, width_nav_multiplier, height_nav_multiplier)
            if arg.iconPath is not None:
                button.setIcon(QtGui.QIcon(arg.iconPath))
            button.clicked.connect(partial(self.handle_button_click, arg))
            self.addWidget(button)
            
    def handle_button_click(self, display_mode : IconEnum):
        self.unpress_buttons(display_mode.index)
        self.clicked_display_signal.emit(display_mode)

    def unpress_buttons(self, index):
        for i in range(self.count()):    
            if i != index:
                item = self.itemAt(i)

                if item is not None and isinstance(item.widget(), MvgCalcNavButton):
                    nav_button = item.widget()
                    nav_button.remove_pressed() 
                
                
        
    