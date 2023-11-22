#file for unit_converter class
from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtCore import pyqtSignal
from .unit_main import Ui_unit_converter
from gui.screen.unit_listboxes.measures_listbox import measuresListbox

class UnitConverter(QWidget):
    display_listbox = pyqtSignal()
    display_units_1 = pyqtSignal()
    display_units_2 = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        # use the Ui_login_form
        self.ui = Ui_unit_converter()       
        self.ui.setupUi(self)   

        self.ui.measures_listbox.clicked.connect(self.handle_button_click)
        self.ui.unit_listbox_1.clicked.connect(self.handle_unit_1)
        self.ui.unit_listbox_2.clicked.connect(self.handle_unit_2)
        #self.ui.unit_listbox_1.clicked.connect(display_unit_listbox)
        #self.ui.unit_listbox_2.clicked.connect(display_unit_listbox)
        # Add widgets to the stacked widget
    
        
        # show the login window
        #self.show()
    
    def handle_button_click(self):
        #need to change this
        self.display_listbox.emit()
    
    def handle_unit_1(self):
        self.display_units_1.emit()
    
    def handle_unit_2(self):
        self.display_units_2.emit()

    def display_measures(self):
        #display units to choose from given what measurement we are doing
        pass

    def switch_widget(self):
        current_index = self.stacked_widget.currentIndex()

        # Toggle between the two widgets
        if current_index == 0:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(0)
        #display listbox to choose what measurement to convert
