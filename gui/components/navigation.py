from functools import partial

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import  QHBoxLayout

from lib.enums.modes import DisplayModes

from gui.components.button import MvgCalcButton

class NavBar(QHBoxLayout):

    clicked_display_signal = pyqtSignal(DisplayModes)

    def __init__(self, *args : DisplayModes):
        super().__init__()

        for arg  in args:
            button = MvgCalcButton(arg.textSymbol)
            button.button_click_signal.connect(partial(self.handle_button_click, arg))
            self.addWidget(button)
            
    def handle_button_click(self, display_type : DisplayModes):

        self.clicked_display_signal.emit(display_type)