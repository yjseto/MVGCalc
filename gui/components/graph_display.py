from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect
from gui.components.button import MvgCalcButton
from lib.enums.keys import *
from lib.models.user_input import UserInput
from lib.models.graph_input import GraphParams
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
import sys
from PyQt5.QtWidgets import *
from gui.components.graphing_keyboard import BasicGrapingKeyboard
from lib.models.user_input import UserInput


class GraphDisplay(PlotWidget):
    def __init__(self, _user_input : UserInput):
        super().__init__()

        
        while UserInput.update_graph_flag == False:

            '''
            to do, when Plot is invoked, we need to plot that function, then return to the waiting loop?
            
            '''
            x = np.linspace(-10,10,1000)
            y = np.sin(np.linspace(0, 4*np.pi, 1000))

            self.plot(x,y)
