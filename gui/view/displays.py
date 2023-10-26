from PyQt5.QtWidgets import *

import numpy as np
from lib.models.result import IResult

from lib.models.user_input import UserInput
from lib.util.evaluator import context

from gui.components.keyboard import BasicKeyboard
from gui.screen.graph import GraphScreen
from gui.util.css import build_css_string

# remove after evaluator linked to displays
from utils.Util import evaluate_graph, evaluate_to_str

class BasicCalcDisplay(QWidget):
    def __init__(self, app):
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
        
        self.display_expression_text = QTextEdit()
        self.keyboard = BasicKeyboard(self.app)
        """
            IMPORTANT: reciever for signal from keyboard when signal is returned the  
            retrieve_updated_user_input_object method is involked.
        """
        self.keyboard.return_result.connect(self.retrieve_result_object)  
        self.keyboard.refresh_expr_screen.connect(self.refresh_expr_screen)  

        layout_main.addWidget(self.display_result_text)
        layout_main.addWidget(self.display_expression_text)
        layout_main.addWidget(self.keyboard)

        self.setLayout(layout_main)

    """
        IMPORTANT: Create a new display that uses the keyboard component 
        1. copy the function below into the new display component
        2. make sure the QTextEdit fields are set to self.text_field_name
        3. call setText(...) for test you would like to display
    """
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

        self.display_expression_text = QTextEdit()
        self.keyboard = BasicKeyboard(self.app)
        
        #self.keyboard.return_plot.connect(self.handle_plot_request)

        """
            IMPORTANT: reciever for signal from keyboard when signal is returned the  
            retrieve_updated_user_input_object method is involked.
        """
        #self.keyboard.updated_user_input_obj_signal.connect(self.retrieve_updated_user_input_object) 

        layout_main.addWidget(self.graph_screen)
        layout_main.addWidget(self.display_expression_text)
        layout_main.addWidget(self.keyboard)

        self.setLayout(layout_main)

    """
        IMPORTANT: Create a new display that uses the keyboard component 
        1. copy the function below into the new display component
        2. make sure the QTextEdit fields are set to self.text_field_name
        3. call setText(...) for test you would like to display
        NOTE currently the UserInput object is being passed back from the
        keyboard component you can pass any type back from emitter except functions
    """
    #def retrieve_updated_user_input_object(self, updated_user_input : UserInput):
        #self.display_result_text.setText(updated_user_input.result)
        #self.display_expression_text.setText(updated_user_input.format_usr_inp_expr_as_str(True))

    def handle_plot_request(self,result : IResult):
        '''
        if result.clear_graph == True:
            self.graph_screen.clear()
            result.clear_graph = False
        else:
        '''
        x = np.linspace(-100,100,3000)
        #function = evaluate_graph('2 * x')
        #print(function)
        #update eval
        y = eval(result.value)
        #print(print("Data type of y:", y.dtype))
        #self.graph_screen.plot(x,y)
        self.graph_screen.plot(x,y,pen = self.graph_screen.pen)
        
            #self.plot_request_signal.emit(self.graph_display)

        #self.graph_display.trigger_plot_request()
#wait on Joel