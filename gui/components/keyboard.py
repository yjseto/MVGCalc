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
    refresh_expr_screen = pyqtSignal()

    def __init__(self, app : MvgCalcApplication):
        super().__init__()

        self.app = app

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Navbar
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        
        self.NavBar = NavBar(KeyboardDisplayMode.FUNCTIONS)
        main_layout.addLayout(self.NavBar)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row1 = QHBoxLayout()
        main_layout.addLayout(row1)
        """
        Clear Button
        """
        clear = MvgCalcButton(ActionKey.CLEAR.textSymbol, self) 
        
        clear.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            border_top_left_radius = "8px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
        
        row1.addWidget(clear)
        clear.button_click_signal.connect(
            partial(self.handle_button_click, ActionKey.CLEAR))       
        """
        Left Parenthesis
        """
        left_parethesis = MvgCalcButton(CharacterInput.LEFT_P.textSymbol, self)       
        
        left_parethesis.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
        
        left_parethesis.button_click_signal.connect(
            partial(self.handle_button_click, CharacterInput.LEFT_P.textEval))
        """
        Right Parenthesis
        """
        right_parethesis = MvgCalcButton(CharacterInput.RIGHT_P.textSymbol, self)                                              
        
        right_parethesis.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px" 
            ))
    
        right_parethesis.button_click_signal.connect(
            partial(self.handle_button_click, CharacterInput.RIGHT_P.textEval))
  
        #add both left and right parenthesis main layout
        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        row1.addLayout(parenthesis_layout)        

        """
        Percent %
        """
        percent = MvgCalcButton("%", self)  

        percent.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#363E4D", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"             
        ))

        row1.addWidget(percent)          
        percent.button_click_signal.connect(partial(self.handle_button_click, '%'))
        
        # x_var = MvgCalcButton(CharacterInput.XVAR.textSymbol,self)                                                   
        # x_var.setStyleSheet(build_css_string(
        #     "QPushButton",
        #     background_color="#363E4D", 
        #     color="#CBE1FF", 
        #     border_radius="2px",
        #     font_family = "roboto", 
        #     font_size = "28px" 
        #     ))  
        # row1.addWidget(x_var)
        # x_var.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.XVAR.textEval))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row2 = QHBoxLayout()
        main_layout.addLayout(row2)
        """
        Seven 7
        """
        seven = MvgCalcButton("7", self)   
        
        seven.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
            ))
        
        row2.addWidget(seven)
        seven.button_click_signal.connect(partial(self.handle_button_click, "7"))

        """
        Eight 8
        """
        eight = MvgCalcButton("8", self)   
        
        eight.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
            ))
        
        row2.addWidget(eight)        
        eight.button_click_signal.connect(partial(self.handle_button_click, "8"))

        """
        Nine 9
        """
        nine = MvgCalcButton("9",self)
        
        nine.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))   
        
        row2.addWidget(nine) 
        nine.button_click_signal.connect(partial(self.handle_button_click, "9"))
        
        """
        Square Root
        """
        sqrt = MvgCalcButton(MathFunction.SQRT.textSymbol,self)
        
        sqrt.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))   
        
        row2.addWidget(sqrt) 
        sqrt.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQRT))
         
        """
        Backspace
        """
        backspace = MvgCalcButton(ActionKey.BACKSPACE.textSymbol,self)
        
        backspace.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))   
        
        row2.addWidget(backspace) 
        backspace.button_click_signal.connect(partial(self.handle_button_click, "sqrt"))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row3 = QHBoxLayout()
        main_layout.addLayout(row3)
        """
        Four 4
        """
        four = MvgCalcButton("4", self)   
        
        four.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        row3.addWidget(four)
        four.button_click_signal.connect(partial(self.handle_button_click, "4"))
        """
        Five 5
        """
        five = MvgCalcButton("5",  self) 
        
        five.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
          
        row3.addWidget(five)   
        five.button_click_signal.connect(partial(self.handle_button_click, "5"))
        """
        Six 6
        """
        six = MvgCalcButton("6",  self) 
        
        six.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
          
        row3.addWidget(six) 
        six.button_click_signal.connect(partial(self.handle_button_click, "6"))
        """
        Squared
        """
        squared = MvgCalcButton(MathFunction.SQUARED.textSymbol,  self)   
        squared.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        row3.addWidget(squared)        
        squared.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQUARED))
        """
        Division
        """
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
    
        row3.addWidget(division)  
        division.button_click_signal.connect(partial(self.handle_button_click, Operator.DIVIDE))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row4 = QHBoxLayout()
        main_layout.addLayout(row4)
        """
        One 1
        """        
        one = MvgCalcButton("1",self)   
        
        one.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        row4.addWidget(one)  
        one.button_click_signal.connect(partial(self.handle_button_click, "1"))
        """
        Two 2
        """  
        two = MvgCalcButton("2",self)   
        two.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        row4.addWidget(two)       
        two.button_click_signal.connect(partial(self.handle_button_click, "2"))
        """
        Three 3
        """  
        three = MvgCalcButton("3",self) 
        
        three.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
          
        row4.addWidget(three)    
        three.button_click_signal.connect(partial(self.handle_button_click, "3"))
        """
        Add +
        """  
        add = MvgCalcButton(Operator.ADD.textSymbol,self)   
        
        add.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        
        row4.addWidget(add)    
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))
        """
        Multiply
        """  
        multiplication = MvgCalcButton(Operator.MULTIPLY.textSymbol, self)  

        multiplication.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))

        row4.addWidget(multiplication) 
        multiplication.button_click_signal.connect(partial(self.handle_button_click, Operator.MULTIPLY))

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIFTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row5 = QHBoxLayout()
        main_layout.addLayout(row5)
        """
        Negitive +/-
        """  
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
        
        row5.addWidget(negitive)
        negitive.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcButton("0",self)
        
        zero.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
           
        row5.addWidget(zero)        
        zero.button_click_signal.connect(partial(self.handle_button_click, "0"))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcButton(".",  self)   
        
        decimal_point.setStyleSheet(build_css_string(
            "QPushButton", 
            background_color = "#242933",
            color = "#CBE1FF",
            border_radius = "2px",
            font_family = "roboto",
            font_size = "28px"
        ))
        
        row5.addWidget(decimal_point)   
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, "."))
        """
        Subtract -
        """ 
        subtract = MvgCalcButton(Operator.SUBTRACT.textSymbol,  self)   
        subtract.setStyleSheet(build_css_string(
            "QPushButton",
            background_color="#0060E5", 
            color="#CBE1FF", 
            border_radius="2px",
            font_family = "roboto", 
            font_size = "28px"
        ))
        row5.addWidget(subtract)          
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))
        """
        Enter
        """         
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
        
        row5.addWidget(enter)   
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

        
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
            self.app.user_input.add_to_list(key_type)
            self.refresh_expr_screen.emit()