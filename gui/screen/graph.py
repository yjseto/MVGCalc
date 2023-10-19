from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import sympy as sp
import math
import numpy as np
from PyQt5.QtWidgets import *
from gui.app import MvgCalcApplication
from gui.components.keyboard import BasicKeyboard
#from gui.components.graphing_keyboard import BasicGrapingKeyboard
#from gui.components.graph_display import GraphDisplay
import sys
from PyQt5.QtWidgets import *
from gui.components.keyboard import BasicKeyboard
from lib.models.user_input import UserInput


'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''

class GraphScreen(PlotWidget):
    def __init__(self):
        super().__init__()
        