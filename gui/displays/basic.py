
import sys
from PyQt5.QtWidgets import *
from gui.components.keyboard import BasicKeyboard
from lib.models.user_input import UserInput


class BasicCalcDisplay(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        #main container contains all ui components for basic calc display
        widget_main = QWidget()
        #create vertical box structure to place widget components
        layout_main = QVBoxLayout()

        self.display_result_text = QTextEdit()

        self.display_expression_text = QTextEdit()
        self.keyboard = BasicKeyboard(self.app.user_input)
        """
            IMPORTANT: reciever for signal from keyboard when signal is returned the  
            retrieve_updated_user_input_object method is involked.
        """
        self.keyboard.updated_user_input_obj_signal.connect(self.retrieve_updated_user_input_object)  

        layout_main.addWidget(self.display_result_text)
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
        self.display_result_text.setText(updated_user_input.result)
        self.display_expression_text.setText(updated_user_input.format_usr_inp_expr_as_str(True))