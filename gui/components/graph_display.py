from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect
from gui.components.button import MvgCalcKeyButton, EnterButton, ClearInputButton, PercentButton
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


class GraphDisplay(PlotWidget):
    def __init__(self, _user_input : UserInput,function : GraphParams):
        super().__init__()
    
        x = np.linspace(-10,10,1000)
        y = function(x)


    
        pass