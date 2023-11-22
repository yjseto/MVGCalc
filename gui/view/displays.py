from typing import Optional

from PyQt5.QtWidgets import *

import pyqtgraph as pg
import numpy as np

from lib.enums.keys import ActionKey
from lib.models.result import GraphResult, ResultBase

from gui.components.textarea import MvgCalcExpressionTextField
from gui.containers.app import MvgCalcApplication
from gui.containers.controller import KeyInputController
from gui.screen.graph import GraphScreen

"""
    IMPORTANT: reciever for signal from keyboard when signal is returned the  
    retrieve_updated_user_input_object method is involked.
"""
class MvgCalcDisplayBase(QWidget):
    def __init__(self, app : MvgCalcApplication):
        super().__init__()
        self.app = app

        #create vertical box structure to place widget components
        self.layout_main = QVBoxLayout()
        self.layout_main.setContentsMargins(2, 0, 2, 0)

        self.textfield_expression = MvgCalcExpressionTextField()
        self.keyboard = KeyInputController(self.app)

        self.keyboard.refresh_expr_screen.connect(self.refresh_expr_screen)  

    def refresh_expr_screen(self, action : Optional[ActionKey] = None):

        if action == ActionKey.UP or action == ActionKey.DOWN:
            self.app.user_input = self.keyboard.hist_expr_display.hist_expr_listbox.update(action)
            self.textfield_expression.setText(self.app.user_input.format_usr_inp_expr_as_str(True))
        else:
            self.app.h_pos = self.textfield_expression.update(self.app.user_input, action)

class BasicCalcDisplay(MvgCalcDisplayBase):
    def __init__(self, app : MvgCalcApplication):
        super().__init__(app)
        
        self.display_result_text = QTextEdit()
        self.display_result_text.setReadOnly(True)
        
        self.display_expression_text = MvgCalcExpressionTextField()
        
        self.keyboard.return_result.connect(self.retrieve_result_object)  

        self.layout_main.addWidget(self.display_result_text)
        self.layout_main.addWidget(self.textfield_expression)
        self.layout_main.addWidget(self.keyboard)

        self.setLayout(self.layout_main)

    def retrieve_result_object(self, result : ResultBase):
        if result.success == False:
            self.display_result_text.setText(result.get_formatted_error_msg_list())
        else:
            self.display_result_text.setText(result.value)
            self.textfield_expression.setText(result.expression)


'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''

class GraphDisplay(MvgCalcDisplayBase):
    def __init__(self, app : MvgCalcApplication):
        super().__init__(app)

        self.x = np.linspace(-100,100,3000)
        self.graph_config = {'x': self.x,
                             'np': np, 
                             'sin': np.sin, 
                             'cos': np.cos, 
                             'tan': np.tan,
                             'asin': np.arcsin,
                             'acos': np.arccos,
                             'atan':np.arctan,
                             'log': np.log10,
                             'ln' : np.emath.log}
        #support for additional functions can be added to this dictionary
        self.pen = pg.mkPen(color = 'w', width = 1.5) #sets the style of the line we plot on the graph

        self.graph_screen = GraphScreen()

        self.keyboard.return_result.connect(self.retrieve_result_object)
        self.keyboard.clear_graph.connect(self.clear_graph_screen)

        self.layout_main.addWidget(self.graph_screen)
        self.layout_main.addWidget(self.textfield_expression)
        self.layout_main.addWidget(self.keyboard)

        self.setLayout(self.layout_main)
    
    def clear_graph_screen(self):
        self.graph_screen.clear()

    def retrieve_result_object(self, result : GraphResult):

        if result.success == True:
            #x = result.x
            #y = eval(result.y)
            y = eval(result.y, self.graph_config)
            self.graph_screen.plot(self.x,y,pen = self.pen)
        else:
            print(result.error_msgs[0])
