#from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel #, QScrollArea, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MvgCalcExpressionTextField(QLabel):
    def __init__(self, ):
        super().__init__() 

        #self.layout = QVBoxLayout(self)

        # Create a QTextEdit widget
        #self.text_edit = QTextEdit(self)
        
        custom_font = QFont("roboto", 28)
        self.setFont(custom_font)
        self.setMaximumHeight(self.fontMetrics().height())

        #self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Place the QTextEdit widget inside a QScrollArea
        # scroll_area = QScrollArea(self)
        # scroll_area.setWidget(self.text_edit)

        # Add the QScrollArea to the layout
        #self.layout.addWidget(scroll_area)


        