import math
from PyQt5.QtWidgets import *

import numpy as np
from lib.models.result import GraphResult, IResult
from gui.components.textarea import MvgCalcExpressionTextField

from gui.containers.app import MvgCalcApplication
from gui.components.keyboard import Keyboard
from gui.screen.graph import GraphScreen
from gui.util.css import build_css_string

# remove after evaluator linked to displays
from utils.Util import evaluate_graph, evaluate_to_str

"""
    IMPORTANT: reciever for signal from keyboard when signal is returned the  
    retrieve_updated_user_input_object method is involked.
"""

class BasicCalcDisplay(QWidget):
    def __init__(self, app : MvgCalcApplication):
        super().__init__()
        self.app = app

        #create vertical box structure to place widget components
        layout_main = QVBoxLayout()

        self.display_result_text = QTextEdit()
        self.display_result_text.setStyleSheet(build_css_string(
            "QTextEdit",
            background_color= "#161A20",
            color= "#FFFFFF"
            ))
        
        self.display_expression_text = MvgCalcExpressionTextField()
        self.keyboard = Keyboard(self.app)

        self.keyboard.return_result.connect(self.retrieve_result_object)  
        self.keyboard.refresh_expr_screen.connect(self.refresh_expr_screen)  

        layout_main.addWidget(self.display_result_text)
        layout_main.addWidget(self.display_expression_text)
        layout_main.addWidget(self.keyboard)

        self.setLayout(layout_main)

    def retrieve_result_object(self, result : IResult):
        if result.success == False:
            error_str = ""
            for error in result.error_msgs:
                error_str = error_str + str(error) + '\n'    
            self.display_result_text.setText(error_str)
        else:
            self.display_result_text.setText(result.value)
            self.display_expression_text.setText(result.expression)

    def refresh_expr_screen(self):
        self.display_expression_text.setText(
            self.app.user_input.format_usr_inp_expr_as_str(True))

'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''

class GraphDisplay(QWidget):
    def __init__(self,app):
        super().__init__()
        self.app = app

        self.graph_screen = GraphScreen()

        layout_main = QVBoxLayout()

        self.display_expression_text = MvgCalcExpressionTextField()
        self.keyboard = Keyboard(self.app)

        self.keyboard.return_result.connect(self.retrieve_result_object)
        self.keyboard.refresh_expr_screen.connect(self.refresh_expr_screen)
        self.keyboard.clear_graph.connect(self.clear_graph_screen)

        layout_main.addWidget(self.graph_screen)
        layout_main.addWidget(self.display_expression_text)
        layout_main.addWidget(self.keyboard)

        self.setLayout(layout_main)

    #def retrieve_updated_user_input_object(self, updated_user_input : UserInput):
        #self.display_result_text.setText(updated_user_input.result)
        #self.display_expression_text.setText(updated_user_input.format_usr_inp_expr_as_str(True))
    def refresh_expr_screen(self):
        self.display_expression_text.setText(
            self.app.user_input.format_usr_inp_expr_as_str(True))
    
    def clear_graph_screen(self):
        self.graph_screen.clear()

    def retrieve_result_object(self,result : GraphResult):
        if result.success == False:
            print('NOT IMPLEMENTED')
        else:
            x = result.x
            #y = eval(result.y)
            #{'x': x,'np': np, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,'asin': np.arcsin,'acos': np.arccos,'atan':np.arctan})
            y = eval(result.y, {'x': x,'np': np, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,'asin': np.arcsin,'acos': np.arccos,'atan':np.arctan})
            self.graph_screen.plot(x,y,pen = self.graph_screen.pen)
