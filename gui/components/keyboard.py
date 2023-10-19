import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from utils.Util import evaluate_to_str,evaluate_graph
import numpy as np
from gui.components.button import MvgCalcButton
from lib.enums.keys import *
from lib.models.user_input import UserInput

from gui.util.css import build_css_string

class BasicKeyboard(QWidget):

    #after button click return display text including updated inputs
    updated_user_input_obj_signal = pyqtSignal(UserInput)

    def __init__(self, user_input : UserInput):
        super().__init__()

        self.user_input = user_input

        grid = QGridLayout()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        clear = MvgCalcButton(ActionKey.CLEAR.textSymbol, self.user_input, self) 
        
        clear.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
        
        grid.addWidget(clear,0,0)
        clear.button_click_signal.connect(partial(self.handle_button_click, ActionKey.CLEAR))       


#         QPushButton {\n"
# "    background-color: #363E4D;\n"
# "    color: #CBE1FF;\n"
# "    border-radius: 2px;\n"
# "    font-family: roboto;\n"
# "    font-size: 28px;\n"
# "   }\n"


        left_parethesis = MvgCalcButton(CharacterInput.LEFT_P.textSymbol, self.user_input,self)       
        left_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.LEFT_P.textEval))

        right_parethesis = MvgCalcButton(CharacterInput.RIGHT_P.textSymbol, self.user_input, self)                                              
        right_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.RIGHT_P.textEval))

        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        grid.addLayout(parenthesis_layout,0,1)        


        # TODO replaced with X var for moro's testing need to add % enum
        # percent = MvgCalcButton("%",self.user_input,self)                                              
        # grid.addWidget(percent,0,2)          
        # right_parethesis.button_click_signal.connect(partial(self.handle_button_click, '%'))
        
        x_var = MvgCalcButton(CharacterInput.XVAR.textSymbol,self.user_input,self)                                              
        grid.addWidget(x_var,0,2)
        x_var.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.XVAR.textEval))

        division = MvgCalcButton(Operator.DIVIDE.textSymbol,self.user_input,self)                                              
        grid.addWidget(division,0,3)
        division.button_click_signal.connect(partial(self.handle_button_click, Operator.DIVIDE))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        seven = MvgCalcButton("7", self.user_input, self)   
        grid.addWidget(seven,1,0)
        seven.button_click_signal.connect(partial(self.handle_button_click, "7"))

        eight = MvgCalcButton("8", self.user_input,self)   
        grid.addWidget(eight,1,1)        
        eight.button_click_signal.connect(partial(self.handle_button_click, "8"))

        nine = MvgCalcButton("9",self.user_input,self)   
        grid.addWidget(nine,1,2) 
        nine.button_click_signal.connect(partial(self.handle_button_click, "9"))

        multiplication = MvgCalcButton(Operator.MULTIPLY.textSymbol, self.user_input, self)   
        grid.addWidget(multiplication,1,3)
        multiplication.button_click_signal.connect(partial(self.handle_button_click, Operator.MULTIPLY))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        four = MvgCalcButton("4",self.user_input, self)   
        grid.addWidget(four,2,0)
        four.button_click_signal.connect(partial(self.handle_button_click, "4"))

        five = MvgCalcButton("5", self.user_input, self)   
        grid.addWidget(five,2,1)   
        five.button_click_signal.connect(partial(self.handle_button_click, "5"))

        six = MvgCalcButton("6", self.user_input, self)   
        grid.addWidget(six,2,2) 
        six.button_click_signal.connect(partial(self.handle_button_click, "6"))

        subtract = MvgCalcButton(Operator.SUBTRACT.textSymbol, self.user_input, self)   
        grid.addWidget(subtract,2,3)        
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        one = MvgCalcButton("1",self.user_input,self)   
        grid.addWidget(one,3,0)
        one.button_click_signal.connect(partial(self.handle_button_click, "1"))

        two = MvgCalcButton("2",self.user_input,self)   
        grid.addWidget(two,3,1)        
        two.button_click_signal.connect(partial(self.handle_button_click, "2"))

        three = MvgCalcButton("3",self.user_input,self)   
        grid.addWidget(three,3,2) 
        three.button_click_signal.connect(partial(self.handle_button_click, "3"))

        add = MvgCalcButton(Operator.ADD.textSymbol,self.user_input,self)   
        grid.addWidget(add,3,3)
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIFTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        negitive = MvgCalcButton(CharacterInput.NEGATIVE.textSymbol,self.user_input, self)  
        grid.addWidget(negitive,4,0)
        negitive.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))

        zero = MvgCalcButton("0",self.user_input,self)   
        grid.addWidget(zero,4,1)        
        zero.button_click_signal.connect(partial(self.handle_button_click, "0"))

        decimal_point = MvgCalcButton(".", self.user_input, self)   
        grid.addWidget(decimal_point,4,2) 
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, "."))

        enter = MvgCalcButton(ActionKey.ENTER.textSymbol, self.user_input, self)   
        grid.addWidget(enter,4,3)
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

        self.setLayout(grid)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    click handler functions
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def handle_button_click(self, key_type : Enum | str):

        if key_type == ActionKey.CLEAR:
            self.user_input.clear_list()
            self.user_input.result = ""
        elif key_type == ActionKey.ENTER:
            result = evaluate_to_str(self.user_input.format_usr_inp_expr_as_str()) 
            self.user_input.clear_list()        #clears the list ready for a new calculation
            self.user_input.result = result  

        elif isinstance(key_type, Enum) or  isinstance(key_type, str):
            self.user_input.clear_result()
            self.user_input.add_to_list(key_type)         

        self.updated_user_input_obj_signal.emit(self.user_input)
            



'''
Made this as a separate class in order to add a Plot button, obviusoly we will want to have
like a small keyboard for this display
'''

class GrapingKeyboard(QWidget):

    #after button click return display text including updated inputs
    updated_user_input_obj_signal = pyqtSignal(UserInput)
    plot_request_signal = pyqtSignal(UserInput)#pass up a value

    def __init__(self, user_input : UserInput):
        super().__init__()
        #self.graph_display = GraphDisplay(user_input)
        self.user_input = user_input
        
        grid = QGridLayout()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        clear = MvgCalcButton(ActionKey.CLEAR.textSymbol, self.user_input, self) 
        grid.addWidget(clear,0,0)
        clear.button_click_signal.connect(partial(self.handle_button_click, ActionKey.CLEAR))       

        left_parethesis = MvgCalcButton(CharacterInput.LEFT_P.textSymbol, self.user_input,self)       
        left_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.LEFT_P.textEval))

        right_parethesis = MvgCalcButton(CharacterInput.RIGHT_P.textSymbol, self.user_input, self)                                              
        right_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.RIGHT_P.textEval))

        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        grid.addLayout(parenthesis_layout,0,1)        


        # TODO replaced with X var for moro's testing need to add % enum
        # percent = MvgCalcButton("%",self.user_input,self)                                              
        # grid.addWidget(percent,0,2)          
        # right_parethesis.button_click_signal.connect(partial(self.handle_button_click, '%'))
        
        x_var = MvgCalcButton(CharacterInput.XVAR.textSymbol,self.user_input,self)                                              
        grid.addWidget(x_var,0,2)
        x_var.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.XVAR.textEval))

        division = MvgCalcButton(Operator.DIVIDE.textSymbol,self.user_input,self)                                              
        grid.addWidget(division,0,3)
        division.button_click_signal.connect(partial(self.handle_button_click, Operator.DIVIDE))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        seven = MvgCalcButton("7", self.user_input, self)   
        grid.addWidget(seven,1,0)
        seven.button_click_signal.connect(partial(self.handle_button_click, "7"))

        eight = MvgCalcButton("8", self.user_input,self)   
        grid.addWidget(eight,1,1)        
        eight.button_click_signal.connect(partial(self.handle_button_click, "8"))

        nine = MvgCalcButton("9",self.user_input,self)   
        grid.addWidget(nine,1,2) 
        nine.button_click_signal.connect(partial(self.handle_button_click, "9"))

        multiplication = MvgCalcButton(Operator.MULTIPLY.textSymbol, self.user_input, self)   
        grid.addWidget(multiplication,1,3)
        multiplication.button_click_signal.connect(partial(self.handle_button_click, Operator.MULTIPLY))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        four = MvgCalcButton("4",self.user_input, self)   
        grid.addWidget(four,2,0)
        four.button_click_signal.connect(partial(self.handle_button_click, "4"))

        five = MvgCalcButton("5", self.user_input, self)   
        grid.addWidget(five,2,1)   
        five.button_click_signal.connect(partial(self.handle_button_click, "5"))

        six = MvgCalcButton("6", self.user_input, self)   
        grid.addWidget(six,2,2) 
        six.button_click_signal.connect(partial(self.handle_button_click, "6"))

        subtract = MvgCalcButton(Operator.SUBTRACT.textSymbol, self.user_input, self)   
        grid.addWidget(subtract,2,3)        
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        one = MvgCalcButton("1",self.user_input,self)   
        grid.addWidget(one,3,0)
        one.button_click_signal.connect(partial(self.handle_button_click, "1"))

        two = MvgCalcButton("2",self.user_input,self)   
        grid.addWidget(two,3,1)        
        two.button_click_signal.connect(partial(self.handle_button_click, "2"))

        three = MvgCalcButton("3",self.user_input,self)   
        grid.addWidget(three,3,2) 
        three.button_click_signal.connect(partial(self.handle_button_click, "3"))

        add = MvgCalcButton(Operator.ADD.textSymbol,self.user_input,self)   
        grid.addWidget(add,3,3)
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIFTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        plot = MvgCalcButton(ActionKey.PLOT.textSymbol,self.user_input, self)  
        grid.addWidget(plot,4,0)
        plot.button_click_signal.connect(partial(self.handle_button_click, ActionKey.PLOT))
        # In your button's click event handler function

        zero = MvgCalcButton("0",self.user_input,self)   
        grid.addWidget(zero,4,1)        
        zero.button_click_signal.connect(partial(self.handle_button_click, "0"))

        decimal_point = MvgCalcButton(".", self.user_input, self)   
        grid.addWidget(decimal_point,4,2) 
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, "."))

        enter = MvgCalcButton(ActionKey.ENTER.textSymbol, self.user_input, self)   
        grid.addWidget(enter,4,3)
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SIXTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        to_the = MvgCalcButton(Operator.EXPONENT.textSymbol,self.user_input, self)  
        grid.addWidget(to_the,5,0)
        to_the.button_click_signal.connect(partial(self.handle_button_click, Operator.EXPONENT))
        # In your button's click event handler function

        sqrt = MvgCalcButton(MathFunction.SQRT.textSymbol,self.user_input,self)   
        grid.addWidget(sqrt,5,1)        
        sqrt.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQRT))

        squared = MvgCalcButton(MathFunction.SQUARED.textSymbol, self.user_input, self)   
        grid.addWidget(squared,5,2) 
        squared.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQUARED))

        sin = MvgCalcButton(Trigonometry.SIN.textSymbol, self.user_input, self)   
        grid.addWidget(sin,5,3)
        sin.button_click_signal.connect(partial(self.handle_button_click, Trigonometry.SIN))

        self.setLayout(grid)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    click handler functions
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #'''
    def handle_button_click(self, key_type : Enum | str):

        if key_type == ActionKey.CLEAR:
            self.user_input.clear_list()

        elif key_type == ActionKey.ENTER:
            result = evaluate_to_str(self.user_input.format_usr_inp_expr_as_str()) 
            self.user_input.clear_list()        #clears the list ready for a new calculation
            self.user_input.result = result
        
        elif key_type == ActionKey.PLOT:

            self.plot_request_signal.emit(self.user_input)
             
            
            #result = evaluate_to_str(self.user_input.format_usr_inp_expr_as_str()) 
            #self.user_input.clear_result()
            #self.user_input.result = result 
            #self.graph_display.trigger_plot_request()

        elif isinstance(key_type, Enum) or  isinstance(key_type, str):
            self.user_input.clear_result()
            self.user_input.add_to_list(key_type)  
            
                   
        self.updated_user_input_obj_signal.emit(self.user_input)
        
    #'''