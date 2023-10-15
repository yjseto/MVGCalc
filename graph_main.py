from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget
import sys  # We need sys so that we can pass argv to QApplication
import os
import sympy as sp
import math
import numpy as np
import sys
from PyQt5.QtWidgets import *
from gui.app import MvgCalcApplication
from gui.components.keyboard import BasicKeyboard
from gui.app import MvgCalcApplication

def function_to_plot(x):
    return 5 * x**2

def main():
    app = MvgCalcApplication(sys.argv)
    window = CustomMainWindow(app)
    window.show()
    sys.exit(app.exec_())

class CustomMainWindow(QtWidgets.QMainWindow):

    def __init__(self, _app,*args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)
        
        '''
        test code
        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot('sin(x)')
        mw.draw()
        '''
        self.app = _app


        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.setWindowTitle("Custom MainWindow with graph Example")

        #widget 1
        custom_widget = BasicKeyboard(self.app.user_input)
        custom_widget.setGeometry(400, 400, 400, 400)
        
        #widget 2
        graph_widget = PlotWidget()
        graph_widget.setGeometry(400, 400, 400, 400)
        
        #create x and y values to plot
        #this way gives a good amount of control over how to plot
        x = np.linspace(0,20,1000)
        y = function_to_plot(x)
        graph_widget.plot(x,y)

        self.layout.addWidget(custom_widget)
        self.layout.addWidget(graph_widget)

        self.centralWidget.setLayout(self.layout)


        


if __name__ == '__main__':
    main()