import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from lib.enums.keys import *
from lib.models.result import IResult
from lib.enums.modes import *
from lib.util.evaluator import context

from gui.containers.app import MvgCalcApplication
from gui.components.button import MvgCalcButton
from gui.components.navigation import NavBar
from gui.util.css import *

class Keyboard(QWidget):

    #after button click return display text including updated inputs
    return_result = pyqtSignal(IResult)
    refresh_expr_screen = pyqtSignal()

    def __init__(self, app : MvgCalcApplication):
        super().__init__()

        self.app = app
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.stack_layout = QStackedWidget()

        self.key_display = KeyboardDisplayMode.BASIC
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Navbar
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        
        self.navbar = NavBar(KeyboardDisplayMode.BASIC,KeyboardDisplayMode.FUNCTIONS)
        self.navbar.clicked_display_signal.connect(self.activate_tab)
        self.main_layout.addLayout(self.navbar)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Basic Keys
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.basic_keys = BasicKeyboard()
        self.stack_layout.addWidget(self.basic_keys)
        self.basic_keys.button_click_signal_from_keyboard.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Function Keys
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.func_keys = FunctionKeyboard()
        self.stack_layout.addWidget(self.func_keys)
        self.func_keys.button_click_signal_from_keyboard.connect(self.handle_button_click)

        self.main_layout.addWidget(self.stack_layout)

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # click handler functions
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def handle_button_click(self, key_type : Enum):
        #result: IResult
        if key_type == ActionKey.CLEAR:
            self.app.user_input.clear_list()
            self.refresh_expr_screen.emit()
        elif key_type == ActionKey.ENTER:
            result = context(DisplayMode.BASIC, self.app.user_input) 
            self.app.user_input.clear_list()
            self.return_result.emit(result) 
        elif isinstance(key_type, Enum):
            self.app.user_input.add_to_list(key_type)
            self.refresh_expr_screen.emit()

    def activate_tab(self, display_type : KeyboardDisplayMode):
        self.key_display = display_type
        self.stack_layout.setCurrentIndex(display_type.index)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BASIC KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class BasicKeyboard(QWidget):

    button_click_signal_from_keyboard = pyqtSignal(Enum)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row1 = QHBoxLayout()
        main_layout.addLayout(row1)
        """
        Clear Button
        """
        clear = MvgCalcButton(ActionKey.CLEAR.textSymbol, self) 
        clear.setStyleSheet(component_light_grey("QPushButton", border_top_left_radius = "8px"))
        
        row1.addWidget(clear)
        clear.button_click_signal.connect(
            partial(self.handle_button_click, ActionKey.CLEAR))       
        """
        Left Parenthesis
        """
        left_parethesis = MvgCalcButton(CharacterInput.LEFT_P.textSymbol, self)             
        left_parethesis.setStyleSheet(component_light_grey("QPushButton"))
        
        left_parethesis.button_click_signal.connect(
            partial(self.handle_button_click, CharacterInput.LEFT_P.textEval))
        """
        Right Parenthesis
        """
        right_parethesis = MvgCalcButton(CharacterInput.RIGHT_P.textSymbol, self)                                                   
        right_parethesis.setStyleSheet(component_light_grey("QPushButton"))
    
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
        percent.setStyleSheet(component_light_grey("QPushButton"))

        row1.addWidget(percent)          
        percent.button_click_signal.connect(partial(self.handle_button_click, '%'))
        """
        D Pad
        """       
        d_pad = DPad()
        row1.addWidget(d_pad) 
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row2 = QHBoxLayout()
        main_layout.addLayout(row2)
        """
        Seven 7
        """
        seven = MvgCalcButton(NumericInput.SEVEN.textSymbol, self)   
        seven.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(seven)
        seven.button_click_signal.connect(partial(self.handle_button_click, NumericInput.SEVEN))
        """
        Eight 8
        """
        eight = MvgCalcButton(NumericInput.EIGHT.textSymbol, self)   
        eight.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(eight)        
        eight.button_click_signal.connect(partial(self.handle_button_click, NumericInput.EIGHT))
        """
        Nine 9
        """
        nine = MvgCalcButton(NumericInput.NINE.textSymbol,self) 
        nine.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(nine) 
        nine.button_click_signal.connect(partial(self.handle_button_click, NumericInput.NINE))    
        """
        Square Root
        """
        sqrt = MvgCalcButton(MathFunction.SQRT.textSymbol,self)
        sqrt.setStyleSheet(component_blue("QPushButton"))   
        
        row2.addWidget(sqrt) 
        sqrt.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQRT))   
        """
        Backspace
        """
        backspace = MvgCalcButton(ActionKey.BACKSPACE.textSymbol,self)
        backspace.setStyleSheet(component_red("QPushButton")) 
        
        row2.addWidget(backspace) 
        backspace.button_click_signal.connect(partial(self.handle_button_click, ActionKey.BACKSPACE))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row3 = QHBoxLayout()
        main_layout.addLayout(row3)
        """
        Four 4
        """
        four = MvgCalcButton(NumericInput.FOUR.textSymbol, self)   
        four.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(four)
        four.button_click_signal.connect(partial(self.handle_button_click, NumericInput.FOUR))
        """
        Five 5
        """
        five = MvgCalcButton(NumericInput.FIVE.textSymbol,  self)   
        five.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(five)   
        five.button_click_signal.connect(partial(self.handle_button_click, NumericInput.FIVE))
        """
        Six 6
        """
        six = MvgCalcButton(NumericInput.SIX.textSymbol,  self)  
        six.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(six) 
        six.button_click_signal.connect(partial(self.handle_button_click, NumericInput.SIX))
        """
        Squared
        """
        squared = MvgCalcButton(MathFunction.SQUARED.textSymbol,  self)   
        squared.setStyleSheet(component_blue("QPushButton"))

        row3.addWidget(squared)        
        squared.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQUARED))
        """
        Division
        """
        division = MvgCalcButton(Operator.DIVIDE.textSymbol,self)                                              
        division.setStyleSheet(component_blue("QPushButton"))
    
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
        one = MvgCalcButton(NumericInput.ONE.textSymbol,self)   
        one.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(one)  
        one.button_click_signal.connect(partial(self.handle_button_click, NumericInput.ONE))
        """
        Two 2
        """  
        two = MvgCalcButton(NumericInput.TWO.textSymbol,self)   
        two.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(two)       
        two.button_click_signal.connect(partial(self.handle_button_click, NumericInput.TWO))
        """
        Three 3
        """  
        three = MvgCalcButton(NumericInput.THREE.textSymbol,self) 
        three.setStyleSheet(component_dark_grey("QPushButton"))
          
        row4.addWidget(three)    
        three.button_click_signal.connect(partial(self.handle_button_click, NumericInput.THREE))
        """
        Add +
        """  
        add = MvgCalcButton(Operator.ADD.textSymbol,self)   
        add.setStyleSheet(component_blue("QPushButton"))
        
        row4.addWidget(add)    
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))
        """
        Multiply
        """  
        multiplication = MvgCalcButton(Operator.MULTIPLY.textSymbol, self)  
        multiplication.setStyleSheet(component_blue("QPushButton"))

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
        negitive.setStyleSheet(component_light_grey("QPushButton", border_bottom_left_radius = "8px"))
        
        row5.addWidget(negitive)
        negitive.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcButton(NumericInput.ZERO.textSymbol,self)
        zero.setStyleSheet(component_dark_grey("QPushButton"))
           
        row5.addWidget(zero)        
        zero.button_click_signal.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcButton(".",  self)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, "."))
        """
        Subtract -
        """ 
        subtract = MvgCalcButton(Operator.SUBTRACT.textSymbol,  self)   
        subtract.setStyleSheet(component_blue("QPushButton"))

        row5.addWidget(subtract)          
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))
        """
        Enter
        """         
        enter = MvgCalcButton(ActionKey.ENTER.textSymbol,  self)   
        enter.setStyleSheet(component_blue("QPushButton",border_bottom_right_radius = "8px"))
        
        row5.addWidget(enter)   
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

    def handle_button_click(self, key_type : Enum):
        self.button_click_signal_from_keyboard.emit(key_type)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DIRECTIONAL KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class DPad(QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        up_arrow = MvgCalcButton(ActionKey.UP.textSymbol)  
        up_arrow.setStyleSheet(component_light_grey("QPushButton"))
        main_layout.addWidget(up_arrow)
    
        horizontal_layout = QHBoxLayout()
        left_arrow = MvgCalcButton(ActionKey.LEFT.textSymbol)
        left_arrow.setStyleSheet(component_light_grey("QPushButton"))  
        horizontal_layout.addWidget(left_arrow)
        
        right_arrow = MvgCalcButton(ActionKey.RIGHT.textSymbol)
        right_arrow.setStyleSheet(component_light_grey("QPushButton"))  
        horizontal_layout.addWidget(right_arrow)
        main_layout.addLayout(horizontal_layout)
        
        down_arrow = MvgCalcButton(ActionKey.DOWN.textSymbol)  
        down_arrow.setStyleSheet(component_light_grey("QPushButton"))
        main_layout.addWidget(down_arrow)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
FUNCTION KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class FunctionKeyboard(QWidget):

    button_click_signal_from_keyboard = pyqtSignal(Enum)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row1 = QHBoxLayout()
        main_layout.addLayout(row1)


        x_var = MvgCalcButton(CharacterInput.XVAR.textSymbol,self) 
        x_var.setStyleSheet(component_light_grey("QPushButton"))
        row1.addWidget(x_var)
        x_var.button_click_signal.connect(
            partial(self.handle_button_click, CharacterInput.XVAR))  

    def handle_button_click(self, key_type : Enum):
        self.button_click_signal_from_keyboard.emit(key_type)

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