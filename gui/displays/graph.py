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
#from gui.components.graphing_keyboard import BasicGrapingKeyboard
#from gui.components.graph_display import GraphDisplay
import sys
from PyQt5.QtWidgets import *
from gui.components.keyboard import BasicKeyboard, GrapingKeyboard
from lib.models.user_input import UserInput
from gui.screen.graph import GraphScreen
from utils.Util import evaluate_graph, evaluate_to_str


'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''

class GraphDisplay(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app

        #main container contains all ui components for basic calc display
        widget_main = QWidget()
        #create vertical box structure to place widget components
        layout_main = QVBoxLayout()

        self.graph_screen = GraphScreen()
        

        self.display_expression_text = QTextEdit()
        self.keyboard = GrapingKeyboard(self.app.user_input) #might not work
        
        self.keyboard.plot_request_signal.connect(self.handle_plot_request)

        """
            IMPORTANT: reciever for signal from keyboard when signal is returned the  
            retrieve_updated_user_input_object method is involked.
        """
        self.keyboard.updated_user_input_obj_signal.connect(self.retrieve_updated_user_input_object) 
        
        #Connect plot request
        
    

        layout_main.addWidget(self.graph_screen)
        layout_main.addWidget(self.display_expression_text)
        layout_main.addWidget(self.keyboard)

        widget_main.setLayout(layout_main)

        self.setCentralWidget(widget_main)

    """
        IMPORTANT: Create a new display that uses the keyboard component 
        1. copy the function below into the new display component
        2. make sure the QTextEdit fields are set to self.text_field_name
        3. call setText(...) for test you would like to display
        NOTE currently the UserInput object is being passed back from the
        keyboard component you can pass any type back from emitter except functions
    """
    def retrieve_updated_user_input_object(self, updated_user_input : UserInput):
        #self.display_result_text.setText(updated_user_input.result)
        self.display_expression_text.setText(updated_user_input.format_usr_inp_expr_as_str(True))

    def handle_plot_request(self,updated_user_input: UserInput):
        to_graph = updated_user_input.format_usr_inp_expr_as_str()
        result = evaluate_to_str(to_graph)
        x = np.linspace(-20,20,1000)
        #function = evaluate_graph('2 * x')
        #print(function)
        #update eval
        y = eval(result)
        #print(print("Data type of y:", y.dtype))
        self.graph_screen.plot(x,y)
        #self.plot_request_signal.emit(self.graph_display)

        #self.graph_display.trigger_plot_request()
#wait on Joel