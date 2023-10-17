from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,QRect
from gui.components.button import MvgCalcButton
from lib.enums.keys import *
from lib.models.graph_input import GraphParams
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget
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
import sys
from PyQt5.QtWidgets import *
#from gui.components.graphing_keyboard import BasicGrapingKeyboard
from lib.models.user_input import UserInput


class GraphDisplay(QWidget):
    plot_request_signal = pyqtSignal()

    def __init__(self, _user_input : UserInput):
        super().__init__()
        self.graph_widget = PlotWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.graph_widget)
        self.setLayout(layout)

        self.plot_request_signal.connect(self.trigger_plot_request)
        
        #while UserInput.update_graph_flag == False:

        '''
        to do, when Plot is invoked, we need to plot that function, then return to the waiting loop?
            
        '''
        self.x = np.linspace(-10,10,1000)
        self.y = None

        #self.plot(x,y)

    def update_graph(self,function):
        
        self.y = function
        self.graph_widget.plot(self.x,self.y)     
        
        pass

    #def update_graph(self,function):
        #pass
    def handle_plot_request(self):
        # Get the data for the graph, for example using self.user_input
        func_to_plot = self.user_input.convert_usr_inp_exp_as_func()
    
        # Update the graph with the new data
        self.update_graph(func_to_plot)
    
    # Clear any other data if needed
        self.user_input.clear_list()

    def trigger_plot_request(self):
        self.plot_request_signal.emit()
