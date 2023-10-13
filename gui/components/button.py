from PyQt5.QtWidgets import QPushButton
from lib.models.user_input import UserInput
from utils.Util import evaluate_percentage,evaluate_to_str

class MvgCalcKeyButton(QPushButton):
    def __init__(self, text, _value, _user_input : UserInput, parent=None):
        super().__init__(text, parent)

        self.user_input = _user_input
        self.value = _value
        
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #0060E5;
                color: #CBE1FF;
                border-radius: 2px;
                border-top-right-radius: 8px;
                font-family: roboto;
                font-size: 38px;
            }
            """
        )      

    def mousePressEvent(self, event):
        self.user_input.add_to_list(self.value)
        print(self.user_input.user_input_list)    
        print(self.user_input.__str__)


class EnterButton(QPushButton):
    def __init__(self, text, _value, _user_input : UserInput,  parent=None):
        super().__init__(text, parent)

        self.user_input = _user_input
        self.value = _value
        
        
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #0060E5;
                color: #CBE1FF;
                border-radius: 2px;
                border-top-right-radius: 8px;
                font-family: roboto;
                font-size: 38px;
            }
            """
        )      

    def mousePressEvent(self, event):
        result = evaluate_to_str(self.user_input.format_usr_inp_expr_as_str()) 
        self.user_input.clear_list() #clears the list ready for a new calculation
        print(result)

class ClearInputButton(QPushButton):
    def __init__(self, text, _value, _user_input : UserInput,  parent=None):
        super().__init__(text, parent)

        self.user_input = _user_input
        self.value = _value
        
        
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #0060E5;
                color: #CBE1FF;
                border-radius: 2px;
                border-top-right-radius: 8px;
                font-family: roboto;
                font-size: 38px;
            }
            """
        )      

    def mousePressEvent(self, event):
        self.user_input.user_input_list.clear()
        print(self.user_input.user_input_list)

class PercentButton(QPushButton):
    def __init__(self, text, _value, _user_input : UserInput,  parent=None):
        super().__init__(text, parent)

        self.user_input = _user_input
        self.value = _value
        
        
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #0060E5;
                color: #CBE1FF;
                border-radius: 2px;
                border-top-right-radius: 8px;
                font-family: roboto;
                font-size: 38px;
            }
            """
        )      

    def mousePressEvent(self, event):
        result = evaluate_percentage(self.user_input.format_usr_inp_expr_as_str())
        self.user_input.user_input_list.clear() #clears the list ready for a new calculation
        self.user_input.user_input_list.append(result)
        print(result)            
            
