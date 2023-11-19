from functools import partial

from PyQt5.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
    QHBoxLayout
)

from lib.enums.modes import DisplayMode

from gui.components.button import MvgCalcInputButton2
from gui.view.displays import BasicCalcDisplay, GraphDisplay
from gui.util.css import *
from gui.util.setup import *

class MvgCalcMainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle("")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        """
        TODO: Enable Code below to test if window will be auto-resized to fit length and width on
        mobile devices
        """
        # Get the screen dimensions
        # desktop = QDesktopWidget()
        # screen_width = desktop.screenGeometry().width()
        # screen_height = desktop.screenGeometry().height()

        # Set the main window's size
        # window_width = int(screen_width * 1)  # Set to 100% of the screen width
        # window_height = int(screen_height * 1)  # Set to 100% of the screen height
        #self.setFixedSize(window_width, window_height)
        
        self.setFixedSize(391, 828)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.stack_layout = QStackedWidget()
        central_widget.setLayout(self.main_layout)

        #add nav bar button group to top of calculator
        # self.navbar = NavBar(DisplayMode.BASIC, DisplayMode.GRAPH, DisplayMode.UNIT_CONV)
        
        # self.navbar.setContentsMargins(0,0,0,0)
        # self.navbar.clicked_display_signal.connect(self.activate_tab)
        # self.main_layout.addLayout(self.navbar)
        
        self.navbar_layout = QHBoxLayout()
        button1 = MvgCalcInputButton2(DisplayMode.BASIC.textSymbol, width_nav_multiplier, height_nav_multiplier)
        button1.setStyleSheet(component_nav_gray("QPushButton", Border_top_left_radius= "4px", border_bottom_left_radius = "4px"))
        button1.clicked.connect(
            partial(self.activate_tab,DisplayMode.BASIC))
        self.navbar_layout.addWidget(button1)
        
        button2 = MvgCalcInputButton2(DisplayMode.GRAPH.textSymbol, width_nav_multiplier, height_nav_multiplier)
        button2.setStyleSheet(component_nav_gray("QPushButton"))
        button2.clicked.connect(
            partial(self.activate_tab, DisplayMode.GRAPH))
        self.navbar_layout.addWidget(button2)
        
        button3 = MvgCalcInputButton2(DisplayMode.UNIT_CONV.textSymbol, width_nav_multiplier, height_nav_multiplier)
        button3.setStyleSheet(component_nav_gray("QPushButton", border_top_right_radius = "4px", border_bottom_right_radius = "4px"))
        button3.clicked.connect(
            partial(self.activate_tab, DisplayMode.UNIT_CONV))
        self.navbar_layout.addWidget(button3)
        self.main_layout.addLayout(self.navbar_layout)

        # add calculator views
        self.stack_layout.addWidget(BasicCalcDisplay(self.app))
        self.stack_layout.addWidget(GraphDisplay(self.app))

        self.main_layout.addWidget(self.stack_layout)
        

    def activate_tab(self, display_mode : DisplayMode):
        self.app.display_mode = display_mode
        self.stack_layout.setCurrentIndex(display_mode.index)