from PyQt5.QtWidgets import QPushButton
from lib.models.user_input import UserInput
from utils.Util import evaluate_percentage,evaluate_to_str

class MvgCalcKeyButton(QPushButton):
    def __init__(self, text, _value, _list : list, _dim, parent=None):
        super().__init__(text, parent)

        self.list = _list
        self.value = _value
        self.setGeometry(_dim)
        
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
        self.list.append(self.value)
        print(self.list)



class EnterButton(QPushButton):
    def __init__(self, text, _value, _list : list, _dim, parent=None):
        super().__init__(text, parent)

        self.list = _list
        self.value = _value
        self.setGeometry(_dim)
        
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
        user_input = UserInput(self.list)
        format_user_input = user_input.format_usr_inp_expr_as_str()
        result = evaluate_to_str(format_user_input) 
        self.list.clear() #clears the list ready for a new calculation
        print(result)

class ClearInputButton(QPushButton):
    def __init__(self, text, _value, _list : list, _dim, parent=None):
        super().__init__(text, parent)

        self.list = _list
        self.value = _value
        self.setGeometry(_dim)
        
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
        self.list.clear()
        print(self.list)

class PercentButton(QPushButton):
    def __init__(self, text, _value, _list : list, _dim, parent=None):
        super().__init__(text, parent)

        self.list = _list
        self.value = _value
        self.setGeometry(_dim)
        
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
        user_input = UserInput(self.list)
        format_user_input = user_input.format_usr_inp_expr_as_str()
        result = evaluate_percentage(format_user_input)
        self.list.clear() #clears the list ready for a new calculation
        self.list.append(result)
        print(result)            
            
