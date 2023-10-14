from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from pyqtgraph.widgets.MatplotlibWidget import MatplotlibWidget
import sys  # We need sys so that we can pass argv to QApplication
import os
import sympy as sp
import math

class CustomMainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(CustomMainWindow, self).__init__(*args, **kwargs)
        
        '''
        test code
        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot('sin(x)')
        mw.draw()
        '''
        
        self.graphWidget = MatplotlibWidget()
        self.setCentralWidget(self.graphWidget)

        subplot = self.graphWidget.getFigure().add_subplot(111)
        subplot.plot('sin(x)')
        self.graphWidget.draw()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = CustomMainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()