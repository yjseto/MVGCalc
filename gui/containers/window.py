from PyQt5.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
    QDesktopWidget
)

from lib.enums.modes import DisplayMode

from gui.view.displays import BasicCalcDisplay, GraphDisplay
from gui.components.navigation import NavBar

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
        self.setFixedSize(360, 740)

        self.main_layout = QVBoxLayout()
        self.stack_layout = QStackedWidget()
        central_widget.setLayout(self.main_layout)

        #add nav bar button group to top of calculator
        self.navbar = NavBar(DisplayMode.BASIC, DisplayMode.GRAPH)
        self.navbar.clicked_display_signal.connect(self.activate_tab)
        self.main_layout.addLayout(self.navbar)

        # add calculator views
        self.stack_layout.addWidget(BasicCalcDisplay(self.app))
        self.stack_layout.addWidget(GraphDisplay(self.app))

        self.main_layout.addWidget(self.stack_layout)

    def activate_tab(self, display_mode : DisplayMode):
        self.app.display_mode = display_mode
        self.stack_layout.setCurrentIndex(display_mode.index)