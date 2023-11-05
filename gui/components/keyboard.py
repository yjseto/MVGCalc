import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from lib.enums.keys import *
from lib.enums.constants import *
from lib.models.result import IResult
from lib.enums.modes import *
from lib.util.evaluator import evaluate

from gui.containers.app import MvgCalcApplication
from gui.components.button import MvgCalcInputButton, MvgCalcHalfInputButton, MvgCalcInputButton
from gui.components.navigation import NavBar
from gui.util.css import *


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Keyboard

Container component for keyboard button navigation component,
basic keyboard, and functions keyboard.

This keyboard component acts as the controller for user keyboard input.
All signals from child components are recieved and the either a request 
to the evaluator service made or the user_input model is updated.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Keyboard(QWidget):

    #after button click return display text including updated inputs
    return_result = pyqtSignal(IResult)
    refresh_expr_screen = pyqtSignal()
    clear_graph = pyqtSignal()

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
        Basic Keyboard
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.basic_keys = BasicKeyboard()
        self.stack_layout.addWidget(self.basic_keys)
        self.basic_keys.button_click_signal_from_keyboard.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Function Keyboard
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.func_keys = FunctionKeyboard()
        self.stack_layout.addWidget(self.func_keys)
        self.func_keys.button_click_signal_from_keyboard.connect(self.handle_button_click)

        self.main_layout.addWidget(self.stack_layout)

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # click handler functions
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def handle_button_click(self, key_type : BaseEnum):
        #result: IResult
        if key_type == ActionKey.CLEAR:
            self.app.user_input.clear_list()
            self.refresh_expr_screen.emit()
            self.clear_graph.emit()
        elif key_type == ActionKey.BACKSPACE:
            if not self.app.user_input.is_empty():
                self.app.user_input.pop_from_list()
                self.refresh_expr_screen.emit()
        elif key_type == ActionKey.ENTER:
            result = evaluate(self.app.display_mode, self.app.user_input) 
            self.return_result.emit(result)
        elif isinstance(key_type, ActionKey):
            pass
        elif isinstance(key_type, EvalEnum):    
            self.app.user_input.add_to_list(key_type)
            self.refresh_expr_screen.emit()

    def activate_tab(self, display_type : KeyboardDisplayMode):
        self.key_display = display_type
        self.stack_layout.setCurrentIndex(display_type.index)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BASIC KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class BasicKeyboard(QWidget):

    button_click_signal_from_keyboard = pyqtSignal(BaseEnum)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW - Shared Keys
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""     
        shared_keys = SharedKeyRow()
        main_layout.addLayout(shared_keys) 
        shared_keys.button_click_signal_from_shared_keys.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row2 = QHBoxLayout()
        main_layout.addLayout(row2)
        """
        Seven 7
        """
        seven = MvgCalcInputButton(NumericInput.SEVEN.textSymbol)   
        seven.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(seven)
        seven.button_click_signal.connect(partial(self.handle_button_click, NumericInput.SEVEN))
        """
        Eight 8
        """
        eight = MvgCalcInputButton(NumericInput.EIGHT.textSymbol)   
        eight.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(eight)        
        eight.button_click_signal.connect(partial(self.handle_button_click, NumericInput.EIGHT))
        """
        Nine 9
        """
        nine = MvgCalcInputButton(NumericInput.NINE.textSymbol) 
        nine.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(nine) 
        nine.button_click_signal.connect(partial(self.handle_button_click, NumericInput.NINE))    
        """
        Square Root
        """
        sqrt = MvgCalcInputButton(MathFunction.SQRT.get_no_parentheses())
        sqrt.setStyleSheet(component_blue("QPushButton"))   
        
        row2.addWidget(sqrt) 
        sqrt.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQRT))   
        """
        Percent %
        """
        percent = MvgCalcInputButton(Operator.PERCENT.textSymbol)  
        percent.setStyleSheet(component_blue("QPushButton"))

        row2.addWidget(percent)          
        percent.button_click_signal.connect(partial(self.handle_button_click, Operator.PERCENT))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row3 = QHBoxLayout()
        main_layout.addLayout(row3)
        """
        Four 4
        """
        four = MvgCalcInputButton(NumericInput.FOUR.textSymbol)   
        four.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(four)
        four.button_click_signal.connect(partial(self.handle_button_click, NumericInput.FOUR))
        """
        Five 5
        """
        five = MvgCalcInputButton(NumericInput.FIVE.textSymbol)   
        five.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(five)   
        five.button_click_signal.connect(partial(self.handle_button_click, NumericInput.FIVE))
        """
        Six 6
        """
        six = MvgCalcInputButton(NumericInput.SIX.textSymbol)  
        six.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(six) 
        six.button_click_signal.connect(partial(self.handle_button_click, NumericInput.SIX))
        """
        Squared
        """
        squared = MvgCalcInputButton("x\u00b2")   
        squared.setStyleSheet(component_blue("QPushButton"))

        row3.addWidget(squared)        
        squared.button_click_signal.connect(partial(self.handle_button_click, MathFunction.SQUARED))
        """
        Division
        """
        division = MvgCalcInputButton(Operator.DIVIDE.textSymbol)                                              
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
        one = MvgCalcInputButton(NumericInput.ONE.textSymbol)   
        one.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(one)  
        one.button_click_signal.connect(partial(self.handle_button_click, NumericInput.ONE))
        """
        Two 2
        """  
        two = MvgCalcInputButton(NumericInput.TWO.textSymbol)   
        two.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(two)       
        two.button_click_signal.connect(partial(self.handle_button_click, NumericInput.TWO))
        """
        Three 3
        """  
        three = MvgCalcInputButton(NumericInput.THREE.textSymbol) 
        three.setStyleSheet(component_dark_grey("QPushButton"))
          
        row4.addWidget(three)    
        three.button_click_signal.connect(partial(self.handle_button_click, NumericInput.THREE))
        """
        Add +
        """  
        add = MvgCalcInputButton(Operator.ADD.textSymbol)   
        add.setStyleSheet(component_blue("QPushButton"))
        
        row4.addWidget(add)    
        add.button_click_signal.connect(partial(self.handle_button_click, Operator.ADD))
        """
        Multiply
        """  
        multiplication = MvgCalcInputButton(Operator.MULTIPLY.textSymbol)  
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
        negitive = MvgCalcInputButton("\u207A\u2215\u208B")
        negitive.setStyleSheet(component_light_grey("QPushButton", border_bottom_left_radius = "8px"))
        
        row5.addWidget(negitive)
        negitive.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcInputButton(NumericInput.ZERO.textSymbol)
        zero.setStyleSheet(component_dark_grey("QPushButton"))
           
        row5.addWidget(zero)        
        zero.button_click_signal.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcInputButton(CharacterInput.DECIMAL_POINT.textSymbol)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.DECIMAL_POINT))
        """
        Subtract -
        """ 
        subtract = MvgCalcInputButton(Operator.SUBTRACT.textSymbol)   
        subtract.setStyleSheet(component_blue("QPushButton"))

        row5.addWidget(subtract)          
        subtract.button_click_signal.connect(partial(self.handle_button_click, Operator.SUBTRACT))
        """
        Enter
        """         
        enter = MvgCalcInputButton(ActionKey.ENTER.textSymbol)   
        enter.setStyleSheet(component_blue("QPushButton",border_bottom_right_radius = "8px"))
        
        row5.addWidget(enter)   
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER))

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_keyboard.emit(key_type)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
FUNCTION KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class FunctionKeyboard(QWidget):

    button_click_signal_from_keyboard = pyqtSignal(BaseEnum)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW - Shared Keys
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""     
        shared_keys = SharedKeyRow()
        main_layout.addLayout(shared_keys) 
        shared_keys.button_click_signal_from_shared_keys.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Second ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row2 = QHBoxLayout()
        main_layout.addLayout(row2)
        """
        Sin 
        """ 
        sin = MvgCalcInputButton(TrigonometryFunction.SIN.get_no_parentheses())   
        sin.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(sin)
        sin.button_click_signal.connect(partial(self.handle_button_click, TrigonometryFunction.SIN))
        """
        Cos 
        """ 
        cos = MvgCalcInputButton(TrigonometryFunction.COS.get_no_parentheses())   
        cos.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(cos)
        cos.button_click_signal.connect(partial(self.handle_button_click, TrigonometryFunction.COS))
        """
        Tan
        """ 
        tan = MvgCalcInputButton(TrigonometryFunction.TAN.get_no_parentheses())   
        tan.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(tan)
        tan.button_click_signal.connect(partial(self.handle_button_click, TrigonometryFunction.TAN))
        """
        X
        """          
        x_var = MvgCalcInputButton(CharacterInput.XVAR.textSymbol)
        x_var.setStyleSheet(component_blue("QPushButton"))
           
        row2.addWidget(x_var)        
        x_var.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.XVAR))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Third ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row3 = QHBoxLayout()
        main_layout.addLayout(row3)
        """
        Sin Inv
        """ 
        invsin = MvgCalcInputButton(TrigonometryFunction.INVSIN.get_no_parentheses())   
        invsin.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invsin)
        invsin.button_click_signal.connect(partial(self.handle_button_click, TrigonometryFunction.INVSIN))
        """
        Cos Inv 
        """ 
        invcos = MvgCalcInputButton(TrigonometryFunction.INVCOS.get_no_parentheses())   
        invcos.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invcos)
        invcos.button_click_signal.connect(partial(self.handle_button_click, TrigonometryFunction.INVCOS))
        """
        Tan Inv
        """ 
        invtan = MvgCalcInputButton(TrigonometryFunction.INVTAN.get_no_parentheses())   
        invtan.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invtan)
        invtan.button_click_signal.connect(partial(self.handle_button_click, TrigonometryFunction.INVTAN))
        """
        Pi
        """          
        pi = MvgCalcInputButton(MathConstants.PI.textSymbol)
        pi.setStyleSheet(component_blue("QPushButton"))
           
        row3.addWidget(pi)        
        pi.button_click_signal.connect(partial(self.handle_button_click, MathConstants.PI))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Fourth ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row4 = QHBoxLayout()
        main_layout.addLayout(row4)
        """
        Log
        """ 
        log = MvgCalcInputButton(MathFunction.LOG.get_no_parentheses())   
        log.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(log)
        log.button_click_signal.connect(partial(self.handle_button_click, MathFunction.LOG))
        """
        Natural Log
        """ 
        nat_log = MvgCalcInputButton(MathFunction.LOG_NATURAL.get_no_parentheses())   
        nat_log.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(nat_log)
        nat_log.button_click_signal.connect(partial(self.handle_button_click, MathFunction.LOG_NATURAL))
        """
        Pow 10
        """ 
        power = MvgCalcInputButton(MathFunction.POW.textSymbol)   
        power.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(power)
        power.button_click_signal.connect(partial(self.handle_button_click, MathFunction.POW))
        """
        Eulers #
        """          
        e = MvgCalcInputButton(MathConstants.EULERSNUM.textSymbol)
        e.setStyleSheet(component_blue("QPushButton"))
           
        row4.addWidget(e)        
        e.button_click_signal.connect(partial(self.handle_button_click, MathConstants.EULERSNUM))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Fifth ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row5 = QHBoxLayout()
        main_layout.addLayout(row5)
        """
        Negitive +/-
        """  
        negitive = MvgCalcInputButton("\u207A\u2215\u208B")  
        negitive.setStyleSheet(component_light_grey("QPushButton"))
        
        row5.addWidget(negitive)
        negitive.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcInputButton(NumericInput.ZERO.textSymbol)
        zero.setStyleSheet(component_blue("QPushButton"))
           
        row5.addWidget(zero)        
        zero.button_click_signal.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcInputButton(CharacterInput.DECIMAL_POINT.textSymbol)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.button_click_signal.connect(partial(self.handle_button_click, CharacterInput.DECIMAL_POINT))
        """
        Enter
        """         
        enter = MvgCalcInputButton(ActionKey.ENTER.textSymbol)   
        enter.setStyleSheet(component_blue("QPushButton",border_bottom_right_radius = "8px"))
        
        row5.addWidget(enter)   
        enter.button_click_signal.connect(partial(self.handle_button_click, ActionKey.ENTER)) 

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_keyboard.emit(key_type)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
DIRECTIONAL KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class DPad(QWidget):

    button_click_signal_from_d_pad = pyqtSignal(BaseEnum)

    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        up_arrow = MvgCalcInputButton(ActionKey.UP.textSymbol)  
        up_arrow.setStyleSheet(component_light_grey("QPushButton"))
        main_layout.addWidget(up_arrow)
        up_arrow.button_click_signal.connect(partial(self.handle_button_click, ActionKey.UP))
    
        horizontal_layout = QHBoxLayout()
        left_arrow = MvgCalcInputButton(ActionKey.LEFT.textSymbol)
        left_arrow.setStyleSheet(component_light_grey("QPushButton"))  
        horizontal_layout.addWidget(left_arrow)
        left_arrow.button_click_signal.connect(partial(self.handle_button_click, ActionKey.LEFT))
        
        right_arrow = MvgCalcInputButton(ActionKey.RIGHT.textSymbol)
        right_arrow.setStyleSheet(component_light_grey("QPushButton"))  
        horizontal_layout.addWidget(right_arrow)
        main_layout.addLayout(horizontal_layout)
        right_arrow.button_click_signal.connect(partial(self.handle_button_click, ActionKey.RIGHT))
        
        down_arrow = MvgCalcInputButton(ActionKey.DOWN.textSymbol)  
        down_arrow.setStyleSheet(component_light_grey("QPushButton"))
        main_layout.addWidget(down_arrow)
        down_arrow.button_click_signal.connect(partial(self.handle_button_click, ActionKey.DOWN))

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_d_pad.emit(key_type)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Shared Keys Row

this single row of keys will be shared between both basic and functions
keyboards
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class SharedKeyRow(QHBoxLayout):

    button_click_signal_from_shared_keys = pyqtSignal(BaseEnum)

    def __init__(self):
        super().__init__()
        
        """
        Clear Button
        """
        clear = MvgCalcInputButton(ActionKey.CLEAR.textSymbol) 
        clear.setStyleSheet(component_light_grey("QPushButton", border_top_left_radius = "8px",max_width = "20px"))
        
        self.addWidget(clear)
        clear.button_click_signal.connect(
            partial(self.handle_button_click, ActionKey.CLEAR))       
        """
        Left Parenthesis
        """
        left_parethesis = MvgCalcHalfInputButton(CharacterInput.LEFT_P.textSymbol)             
        left_parethesis.setStyleSheet(component_light_grey("QPushButton"))
        
        left_parethesis.button_click_signal.connect(
            partial(self.handle_button_click, CharacterInput.LEFT_P))
        """
        Right Parenthesis
        """
        right_parethesis = MvgCalcHalfInputButton(CharacterInput.RIGHT_P.textSymbol)                                                   
        right_parethesis.setStyleSheet(component_light_grey("QPushButton"))
    
        right_parethesis.button_click_signal.connect(
            partial(self.handle_button_click, CharacterInput.RIGHT_P))
  
        #add both left and right parenthesis main layout
        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        self.addLayout(parenthesis_layout)        
        """
        Backspace
        """
        backspace = MvgCalcInputButton(ActionKey.BACKSPACE.textSymbol)
        backspace.setStyleSheet(component_red("QPushButton")) 
        
        self.addWidget(backspace) 
        backspace.button_click_signal.connect(partial(self.handle_button_click, ActionKey.BACKSPACE))
        """
        D Pad
        """       
        d_pad = DPad()
        self.addWidget(d_pad) 
        d_pad.button_click_signal_from_d_pad.connect(self.handle_button_click)

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_shared_keys.emit(key_type)