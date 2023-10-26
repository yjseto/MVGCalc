import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from gui.components.button import MvgCalcButton
from gui.components.navigation import NavBar
from lib.enums.keys import *
from lib.models.result import IResult
from lib.models.user_input import UserInput

from gui.util.css import build_css_string

from lib.enums.modes import *
from lib.util.evaluator import context

from gui.containers.app import MvgCalcApplication


# class DirectionalButtons(QWidget):
#     def __init__(self):
#         super().__init__()
        
#     main_layout = QVBoxLayout()
#     up_arrow = QPushButton(ActionKey.UP.textSymbol)  
#     main_layout.addWidget(up_arrow)
    
#     # horizontal_layout = QHBoxLayout()
#     # left_arrow = MvgCalcButton(ActionKey.LEFT.textSymbol)  
#     # horizontal_layout.addWidget(left_arrow)
    
#     # right_arrow = MvgCalcButton(ActionKey.RIGHT.textSymbol)  
#     # horizontal_layout.addWidget(right_arrow)
#     # main_layout.addLayout(horizontal_layout)
    
#     # down_arrow = MvgCalcButton(ActionKey.DOWN.textSymbol)  
#     # main_layout.addWidget(down_arrow)
    
#     self.addLayout(main_layout)
    
    
class BasicKeyboard(QWidget):


    #after button click return display text including updated inputs
    return_result = pyqtSignal(IResult)
    #updated_user_input_obj_signal = pyqtSignal(UserInput)

    def __init__(self, app : MvgCalcApplication):
        super().__init__()

        self.app = app
        #self.user_input = user_input

        grid = QGridLayout()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        clear = MvgCalcButton(ActionKey.CLEAR.textSymbol,  self) 
        
        clear.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            border_top_left_radius = "8px",
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


        left_parethesis = MvgCalcButton(CharacterInput.LEFT_P.textSymbol, self)       
        
        left_parethesis.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
        
        left_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.LEFT_P.textEval))

        right_parethesis = MvgCalcButton(CharacterInput.RIGHT_P.textSymbol,  self)                                              
        
        right_parethesis.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
    
        right_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.RIGHT_P.textEval))

        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        grid.addLayout(parenthesis_layout,0,1)        


        # TODO replaced with X var for moro's testing need to add % enum
        # percent = MvgCalcButton("%",self)                                              
        # grid.addWidget(percent,0,2)          
        # right_parethesis.button_click_signal.connect(partial(self.handle_button_click, '%'))
        
        x_var = MvgCalcButton(CharacterInput.XVAR.textSymbol,self)                                              
        
        x_var.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
        
        grid.addWidget(x_var,0,2)
        x_var.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.XVAR.textEval))

        division = MvgCalcButton(Operator.DIVIDE.textSymbol,self)                                              
        
        division.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            border_top_right_radius= "8px",
            font_size = "28px" 
            ))
    
        grid.addWidget(division,0,3)
        division.button_click_signal.connect(partial(self.handle_button_click, Operator.DIVIDE))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        seven = MvgCalcButton("7",  self)   
        
        seven.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
            ))
        
        grid.addWidget(seven,1,0)
        seven.button_click_signal.connect(partial(self.handle_button_click, "7"))

        eight = MvgCalcButton("8", self)   
        
        eight.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
            ))
        
        grid.addWidget(eight,1,1)        
        eight.button_click_signal.connect(partial(self.handle_button_click, "8"))

        nine = MvgCalcButton("9",self)
        
        nine.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))   
        
        grid.addWidget(nine,1,2) 
        nine.button_click_signal.connect(partial(self.handle_button_click, "9"))

        multiplication = MvgCalcButton(Operator.MULTIPLY.textSymbol,  self)   
        
        multiplication.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        
        grid.addWidget(multiplication,1,3)
        multiplication.button_click_signal.connect(partial(self.handle_button_click, Operator.MULTIPLY))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        four = MvgCalcButton("4", self)   
        
        four.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        grid.addWidget(four,2,0)
        four.button_click_signal.connect(partial(self.handle_button_click, "4"))

        five = MvgCalcButton("5",  self) 
        
        five.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
          
        grid.addWidget(five,2,1)   
        five.button_click_signal.connect(partial(self.handle_button_click, "5"))

        six = MvgCalcButton("6",  self) 
        
        six.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
          
        grid.addWidget(six,2,2) 
        six.button_click_signal.connect(partial(self.handle_button_click, "6"))

        subtract = MvgCalcButton(Operator.SUBTRACT.textSymbol,  self)   
        subtract.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        grid.addWidget(subtract,2,3)        
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        one = MvgCalcButton("1",self)   
        
        one.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        grid.addWidget(one,3,0)
        one.button_click_signal.connect(partial(self.handle_button_click, "1"))

        two = MvgCalcButton("2",self)   
        two.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        grid.addWidget(two,3,1)        
        two.button_click_signal.connect(partial(self.handle_button_click, "2"))

        three = MvgCalcButton("3",self) 
        
        three.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
          
        grid.addWidget(three,3,2) 
        three.button_click_signal.connect(partial(self.handle_button_click, "3"))

        add = MvgCalcButton(Operator.ADD.textSymbol,self)   
        
        add.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        
        grid.addWidget(add,3,3)
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIFTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        negitive = MvgCalcButton(CharacterInput.NEGATIVE.textSymbol, self)  
        
        negitive.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            border_bottom_left_radius = "8px",
            font_family = "roboto", 
            font_size = "28px" 
        ))
        
        grid.addWidget(negitive,4,0)
        negitive.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))

        zero = MvgCalcButton("0",self)
        
        zero.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
           
        grid.addWidget(zero,4,1)        
        zero.button_click_signal.connect(partial(self.handle_button_click, "0"))

        decimal_point = MvgCalcButton(".",  self)   
        
        decimal_point.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        grid.addWidget(decimal_point,4,2) 
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, "."))

        enter = MvgCalcButton(ActionKey.ENTER.textSymbol,  self)   
        
        enter.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            border_bottom_right_radius = "8px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        
        grid.addWidget(enter,4,3)
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

        self.setLayout(grid)

        
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # click handler functions
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def handle_button_click(self, key_type : Enum | str):
        #result: IResult
        if key_type == ActionKey.CLEAR:
            self.app.user_input.clear_list()
            self.app.user_input.result = ""
        elif key_type == ActionKey.ENTER:
            result = context(DisplayMode.BASIC, self.app.user_input) 
            self.app.user_input.clear_list()        #clears the list ready for a new calculation
            self.return_result.emit(result)
            #self.app.user_input.result = result  

        elif isinstance(key_type, Enum) or  isinstance(key_type, str):
            self.app.user_input.clear_result()
            self.app.user_input.add_to_list(key_type)

        #self.updated_user_input_obj_signal.emit(self.app.user_input)
            



'''
Made this as a separate class in order to add a Plot button, obviusoly we will want to have
like a small keyboard for this display
'''

class GrapingKeyboard(QWidget):

    #after button click return display text including updated inputs
    #updated_user_input_obj_signal = pyqtSignal(UserInput)
    #plot_request_signal = pyqtSignal(UserInput)#pass up a value
    return_plot = pyqtSignal(IResult)

    def __init__(self, app : MvgCalcApplication):
        super().__init__()
        #self.graph_display = GraphDisplay(user_input)
        #self.user_input = user_input
        self.app = app
        
        grid = QGridLayout()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        clear = MvgCalcButton(ActionKey.CLEAR.textSymbol, self) 
        grid.addWidget(clear,0,0)
        clear.button_click_signal.connect(partial(self.handle_button_click, ActionKey.CLEAR))       

        left_parethesis = MvgCalcButton(CharacterInput.LEFT_P.textSymbol,self)       
        left_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.LEFT_P.textEval))

        right_parethesis = MvgCalcButton(CharacterInput.RIGHT_P.textSymbol, self)                                              
        right_parethesis.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.RIGHT_P.textEval))

        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        grid.addLayout(parenthesis_layout,0,1)        


        # TODO replaced with X var for moro's testing need to add % enum
        # percent = MvgCalcButton("%",self)                                              
        # grid.addWidget(percent,0,2)          
        # right_parethesis.button_click_signal.connect(partial(self.handle_button_click, '%'))
        
        x_var = MvgCalcButton(CharacterInput.XVAR.textSymbol,self)                                              
        grid.addWidget(x_var,0,2)
        x_var.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.XVAR.textEval))

        division = MvgCalcButton(Operator.DIVIDE.textSymbol,self)                                              
        grid.addWidget(division,0,3)
        division.button_click_signal.connect(partial(self.handle_button_click, Operator.DIVIDE))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        seven = MvgCalcButton("7", self)   
        grid.addWidget(seven,1,0)
        seven.button_click_signal.connect(partial(self.handle_button_click, "7"))

        eight = MvgCalcButton("8",self)   
        grid.addWidget(eight,1,1)        
        eight.button_click_signal.connect(partial(self.handle_button_click, "8"))

        nine = MvgCalcButton("9",self)   
        grid.addWidget(nine,1,2) 
        nine.button_click_signal.connect(partial(self.handle_button_click, "9"))

        multiplication = MvgCalcButton(Operator.MULTIPLY.textSymbol, self)   
        grid.addWidget(multiplication,1,3)
        multiplication.button_click_signal.connect(partial(self.handle_button_click, Operator.MULTIPLY))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        four = MvgCalcButton("4", self)   
        grid.addWidget(four,2,0)
        four.button_click_signal.connect(partial(self.handle_button_click, "4"))

        five = MvgCalcButton("5", self)   
        grid.addWidget(five,2,1)   
        five.button_click_signal.connect(partial(self.handle_button_click, "5"))

        six = MvgCalcButton("6", self)   
        grid.addWidget(six,2,2) 
        six.button_click_signal.connect(partial(self.handle_button_click, "6"))

        subtract = MvgCalcButton(Operator.SUBTRACT.textSymbol, self)   
        grid.addWidget(subtract,2,3)        
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        one = MvgCalcButton("1",self)   
        grid.addWidget(one,3,0)
        one.button_click_signal.connect(partial(self.handle_button_click, "1"))

        two = MvgCalcButton("2",self)   
        grid.addWidget(two,3,1)        
        two.button_click_signal.connect(partial(self.handle_button_click, "2"))

        three = MvgCalcButton("3",self)   
        grid.addWidget(three,3,2) 
        three.button_click_signal.connect(partial(self.handle_button_click, "3"))

        add = MvgCalcButton(Operator.ADD.textSymbol,self)   
        grid.addWidget(add,3,3)
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIFTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        plot = MvgCalcButton(ActionKey.PLOT.textSymbol, self)  
        grid.addWidget(plot,4,0)
        plot.button_click_signal.connect(partial(self.handle_button_click, ActionKey.PLOT))
        # In your button's click event handler function

        zero = MvgCalcButton("0",self)   
        grid.addWidget(zero,4,1)        
        zero.button_click_signal.connect(partial(self.handle_button_click, "0"))

        decimal_point = MvgCalcButton(".", self)   
        grid.addWidget(decimal_point,4,2) 
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, "."))

        enter = MvgCalcButton(ActionKey.ENTER.textSymbol, self)   
        grid.addWidget(enter,4,3)
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SIXTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        to_the = MvgCalcButton(Operator.EXPONENT.textSymbol, self)  
        grid.addWidget(to_the,5,0)
        to_the.button_click_signal.connect(partial(self.handle_button_click, Operator.EXPONENT))
        # In your button's click event handler function

        sqrt = MvgCalcButton(MathFunction.SQRT.textSymbol,self)   
        grid.addWidget(sqrt,5,1)        
        sqrt.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQRT))

        squared = MvgCalcButton(MathFunction.SQUARED.textSymbol, self)   
        grid.addWidget(squared,5,2) 
        squared.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQUARED))

        sin = MvgCalcButton(Trigonometry.SIN.textSymbol, self)   
        grid.addWidget(sin,5,3)
        sin.button_click_signal.connect(partial(self.handle_button_click, Trigonometry.SIN))

        self.setLayout(grid)

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    click handler functions
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    #'''
    def handle_button_click(self, key_type : Enum | str):

        if key_type == ActionKey.CLEAR:
            #esult = context(DisplayMode.BASIC, self.app.app.user_input)
            #result.
            #check with Joel on this one
            #self.return_plot.emit(result)
            self.app.user_input.clear_list()

        elif key_type == ActionKey.ENTER:
            result = context(DisplayMode.BASIC, self.app.app.user_input) 
            self.app.user_input.clear_list()        #clears the list ready for a new calculation
            self.app.user_input.result = result
        
        elif key_type == ActionKey.PLOT:
            result = context(DisplayMode.GRAPH, self.app.user_input)
            self.return_plot.emit(result)
            #self.app.user_input.clear_list()
            
            #result = evaluate_to_str(self.user_input.format_usr_inp_expr_as_str()) 
            #self.user_input.clear_result()
            #self.user_input.result = result 
            #self.graph_display.trigger_plot_request()

        elif isinstance(key_type, Enum) or  isinstance(key_type, str):
            self.app.user_input.clear_result()
            self.app.user_input.add_to_list(key_type)  
            
                   
        #self.updated_user_input_obj_signal.emit(self.user_input)
        
        

    

    
        
    #'''