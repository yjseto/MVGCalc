from PyQt5.QtWidgets import QPushButton
from lib.models.user_input import UserInput
from PyQt5.QtCore import pyqtSignal

class MvgCalcButton(QPushButton):

    button_click_signal = pyqtSignal()

    def __init__(self, text, user_input : UserInput, parent=None):
        super().__init__(text, parent)

        self.user_input = user_input
        
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

        #attach click listener to button click event
        self.clicked.connect(self.handle_button_click)


    #transmit signal to the parent component to indicate button has been clicked
    def handle_button_click(self):
        self.button_click_signal.emit()

# class PercentButton(QPushButton):
#     def __init__(self, text, _value, _user_input : UserInput,  parent=None):
#         super().__init__(text, parent)

#         self.user_input = _user_input
#         self.value = _value
        
        
#         self.setStyleSheet(
#             """
#             QPushButton {
#                 background-color: #0060E5;
#                 color: #CBE1FF;
#                 border-radius: 2px;
#                 border-top-right-radius: 8px;
#                 font-family: roboto;
#                 font-size: 38px;
#             }
#             """
#         )      

#     def mousePressEvent(self, event):
#         result = evaluate_percentage(self.user_input.format_usr_inp_expr_as_str())
#         self.user_input.user_input_list.clear() #clears the list ready for a new calculation
#         self.user_input.user_input_list.append(result)
#         print(result)            
            
