from PyQt5.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from lib.enums.modes import DisplayModes

from gui.view.displays import BasicCalcDisplay, GraphDisplay
from gui.components.navigation import NavBar

class MvgCalcMainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.main_layout = QVBoxLayout()
        self.stack_layout = QStackedWidget()
        central_widget.setLayout(self.main_layout)

        #add nav bar button group to top of calculator
        self.navbar = NavBar(DisplayModes.BASIC, DisplayModes.GRAPH)
        self.navbar.clicked_display_signal.connect(self.activate_tab)
        self.main_layout.addLayout(self.navbar)

        # add calculator views
        self.stack_layout.addWidget(BasicCalcDisplay(self.app))
        self.stack_layout.addWidget(GraphDisplay(self.app))

        self.main_layout.addWidget(self.stack_layout)

    def activate_tab(self, display_type : DisplayModes):
        self.stack_layout.setCurrentIndex(display_type.index)