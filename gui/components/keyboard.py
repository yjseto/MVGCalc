import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from lib.enums.keys import *
from lib.util.constants import *
from lib.enums.modes import *

from gui.components.button import MvgCalcInputButton, MvgCalcHalfInputButton, MvgCalcInputButton
from gui.util.css import *
from lib.util.constants import *

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
        main_layout.addWidget(shared_keys) 
        shared_keys.button_click_signal_from_shared_keys.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row2 = QHBoxLayout()
        main_layout.addLayout(row2)
        """
        Seven 7
        """
        seven = MvgCalcInputButton(NumericInput.SEVEN.textSymbol, self)   
        seven.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(seven)
        seven.clicked.connect(partial(self.handle_button_click, NumericInput.SEVEN))
        
        """
        Eight 8
        """
        eight = MvgCalcInputButton(NumericInput.EIGHT.textSymbol, self)   
        eight.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(eight)        
        eight.clicked.connect(partial(self.handle_button_click, NumericInput.EIGHT))
        """
        Nine 9
        """
        nine = MvgCalcInputButton(NumericInput.NINE.textSymbol, self) 
        nine.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(nine) 
        nine.clicked.connect(partial(self.handle_button_click, NumericInput.NINE))    
        """
        Square Root
        """
        sqrt = MvgCalcInputButton(MathFunction.SQRT.get_no_parentheses(), self)
        sqrt.setStyleSheet(component_blue("QPushButton"))   
        
        row2.addWidget(sqrt) 
        sqrt.clicked.connect(partial(self.handle_button_click, MathFunction.SQRT))   
        """
        Percent %
        """
        percent = MvgCalcInputButton(MathFunction.PERCENT.textSymbol, self)  
        percent.setStyleSheet(component_blue("QPushButton"))

        row2.addWidget(percent)          
        percent.clicked.connect(partial(self.handle_button_click, MathFunction.PERCENT))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row3 = QHBoxLayout()
        main_layout.addLayout(row3)
        """
        Four 4
        """
        four = MvgCalcInputButton(NumericInput.FOUR.textSymbol, self)   
        four.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(four)
        four.clicked.connect(partial(self.handle_button_click, NumericInput.FOUR))
        """
        Five 5
        """
        five = MvgCalcInputButton(NumericInput.FIVE.textSymbol, self)   
        five.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(five)   
        five.clicked.connect(partial(self.handle_button_click, NumericInput.FIVE))
        """
        Six 6
        """
        six = MvgCalcInputButton(NumericInput.SIX.textSymbol, self)  
        six.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(six) 
        six.clicked.connect(partial(self.handle_button_click, NumericInput.SIX))
        """
        Squared
        """
        squared = MvgCalcInputButton("x\u00b2")   
        squared.setStyleSheet(component_blue("QPushButton"))

        row3.addWidget(squared)        
        squared.clicked.connect(partial(self.handle_button_click, MathFunction.SQUARED))
        """
        Division
        """
        division = MvgCalcInputButton(Operator.DIVIDE.textSymbol, self)                                              
        division.setStyleSheet(component_blue("QPushButton"))
    
        row3.addWidget(division)  
        division.clicked.connect(partial(self.handle_button_click, Operator.DIVIDE))
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        row4 = QHBoxLayout()
        main_layout.addLayout(row4)
        """
        One 1
        """        
        one = MvgCalcInputButton(NumericInput.ONE.textSymbol, self)   
        one.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(one)  
        one.clicked.connect(partial(self.handle_button_click, NumericInput.ONE))
        """
        Two 2
        """  
        two = MvgCalcInputButton(NumericInput.TWO.textSymbol, self)   
        two.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(two)       
        two.clicked.connect(partial(self.handle_button_click, NumericInput.TWO))
        """
        Three 3
        """  
        three = MvgCalcInputButton(NumericInput.THREE.textSymbol, self) 
        three.setStyleSheet(component_dark_grey("QPushButton"))
          
        row4.addWidget(three)    
        three.clicked.connect(partial(self.handle_button_click, NumericInput.THREE))
        """
        Add +
        """  
        add = MvgCalcInputButton(Operator.ADD.textSymbol, self)   
        add.setStyleSheet(component_blue("QPushButton"))
        
        row4.addWidget(add)    
        add.clicked.connect(partial(self.handle_button_click, Operator.ADD))
        """
        Multiply
        """  
        multiplication = MvgCalcInputButton(Operator.MULTIPLY.textSymbol, self)  
        multiplication.setStyleSheet(component_blue("QPushButton"))

        row4.addWidget(multiplication) 
        multiplication.clicked.connect(partial(self.handle_button_click, Operator.MULTIPLY))
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
        negitive.clicked.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcInputButton(NumericInput.ZERO.textSymbol, self)
        zero.setStyleSheet(component_dark_grey("QPushButton"))
           
        row5.addWidget(zero)        
        zero.clicked.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcInputButton(CharacterInput.DECIMAL_POINT.textSymbol, self)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.clicked.connect(partial(self.handle_button_click, CharacterInput.DECIMAL_POINT))
        """
        Subtract -
        """ 
        subtract = MvgCalcInputButton(Operator.SUBTRACT.textSymbol, self)   
        subtract.setStyleSheet(component_blue("QPushButton"))

        row5.addWidget(subtract)          
        subtract.clicked.connect(partial(self.handle_button_click, Operator.SUBTRACT))
        """
        Enter
        """         
        enter = MvgCalcInputButton(ActionKey.ENTER.textSymbol, self)   
        enter.setStyleSheet(component_blue("QPushButton",border_bottom_right_radius = "8px"))
        
        row5.addWidget(enter)   
        enter.clicked.connect(partial(self.handle_button_click, ActionKey.ENTER))

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
        main_layout.addWidget(shared_keys) 
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
        sin.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.SIN))
        """
        Cos 
        """ 
        cos = MvgCalcInputButton(TrigonometryFunction.COS.get_no_parentheses())   
        cos.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(cos)
        cos.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.COS))
        """
        Tan
        """ 
        tan = MvgCalcInputButton(TrigonometryFunction.TAN.get_no_parentheses())   
        tan.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(tan)
        tan.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.TAN))
        """
        X
        """          
        x_var = MvgCalcInputButton(CharacterInput.XVAR.textSymbol, self)
        x_var.setStyleSheet(component_blue("QPushButton"))
           
        row2.addWidget(x_var)        
        x_var.clicked.connect(partial(self.handle_button_click, CharacterInput.XVAR))
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
        invsin.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.INVSIN))
        """
        Cos Inv 
        """ 
        invcos = MvgCalcInputButton(TrigonometryFunction.INVCOS.get_no_parentheses())   
        invcos.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invcos)
        invcos.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.INVCOS))
        """
        Tan Inv
        """ 
        invtan = MvgCalcInputButton(TrigonometryFunction.INVTAN.get_no_parentheses())   
        invtan.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invtan)
        invtan.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.INVTAN))
        """
        Pi
        """          
        pi = MvgCalcInputButton(MathConstants.PI.textSymbol, self)
        pi.setStyleSheet(component_blue("QPushButton"))
           
        row3.addWidget(pi)        
        pi.clicked.connect(partial(self.handle_button_click, MathConstants.PI))
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
        log.clicked.connect(partial(self.handle_button_click, MathFunction.LOG))
        """
        Natural Log
        """ 
        nat_log = MvgCalcInputButton(MathFunction.LOG_NATURAL.get_no_parentheses())   
        nat_log.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(nat_log)
        nat_log.clicked.connect(partial(self.handle_button_click, MathFunction.LOG_NATURAL))
        """
        Pow 10
        """ 
        power = MvgCalcInputButton(MathFunction.POW.textSymbol, self)   
        power.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(power)
        power.clicked.connect(partial(self.handle_button_click, MathFunction.POW))
        """
        Eulers #
        """          
        e = MvgCalcInputButton(MathConstants.EULERSNUM.textSymbol, self)
        e.setStyleSheet(component_blue("QPushButton"))
           
        row4.addWidget(e)        
        e.clicked.connect(partial(self.handle_button_click, MathConstants.EULERSNUM))
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
        negitive.clicked.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcInputButton(NumericInput.ZERO.textSymbol, self)
        zero.setStyleSheet(component_blue("QPushButton"))
           
        row5.addWidget(zero)        
        zero.clicked.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcInputButton(CharacterInput.DECIMAL_POINT.textSymbol, self)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.clicked.connect(partial(self.handle_button_click, CharacterInput.DECIMAL_POINT))
        """
        Enter
        """         
        enter = MvgCalcInputButton(ActionKey.ENTER.textSymbol, self)   
        enter.setStyleSheet(component_blue("QPushButton",border_bottom_right_radius = "8px"))
        
        row5.addWidget(enter)   
        enter.clicked.connect(partial(self.handle_button_click, ActionKey.ENTER)) 

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
        up_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.UP))
    
        horizontal_layout = QHBoxLayout()
        left_arrow = MvgCalcInputButton(ActionKey.LEFT.textSymbol)
        left_arrow.setStyleSheet(component_light_grey("QPushButton"))  
        horizontal_layout.addWidget(left_arrow)
        left_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.LEFT))
        
        right_arrow = MvgCalcInputButton(ActionKey.RIGHT.textSymbol)
        right_arrow.setStyleSheet(component_light_grey("QPushButton"))  
        horizontal_layout.addWidget(right_arrow)
        main_layout.addLayout(horizontal_layout)
        right_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.RIGHT))
        
        down_arrow = MvgCalcInputButton(ActionKey.DOWN.textSymbol)  
        down_arrow.setStyleSheet(component_light_grey("QPushButton"))
        main_layout.addWidget(down_arrow)
        down_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.DOWN))

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_d_pad.emit(key_type)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Shared Keys Row

this single row of keys will be shared between both basic and functions
keyboards
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class SharedKeyRow(QWidget):

    button_click_signal_from_shared_keys = pyqtSignal(BaseEnum)

    def __init__(self):
        super().__init__()
        
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        """
        Clear Button
        """
        clear = MvgCalcInputButton(ActionKey.CLEAR.textSymbol) 
        clear.setStyleSheet(component_light_grey("QPushButton", border_top_left_radius = "8px",max_width = "20px"))
        main_layout.addWidget(clear)
        clear.clicked.connect(
            partial(self.handle_button_click, ActionKey.CLEAR))       
        """
        Left Parenthesis
        """
        left_parethesis = MvgCalcHalfInputButton(CharacterInput.LEFT_P.textSymbol, width_input_multiplier*0.5, height_input_multiplier, self)             
        left_parethesis.setStyleSheet(component_light_grey("QPushButton"))
        
        left_parethesis.clicked.connect(
            partial(self.handle_button_click, CharacterInput.LEFT_P))
        """
        Right Parenthesis
        """
        right_parethesis = MvgCalcHalfInputButton(CharacterInput.RIGHT_P.textSymbol, width_input_multiplier*0.5, height_input_multiplier, self)                                                   
        right_parethesis.setStyleSheet(component_light_grey("QPushButton"))
    
        right_parethesis.clicked.connect(
            partial(self.handle_button_click, CharacterInput.RIGHT_P))
  
        #add both left and right parenthesis main layout
        parenthesis_layout = QHBoxLayout()       
        parenthesis_layout.addWidget(left_parethesis)
        parenthesis_layout.addWidget(right_parethesis)
        main_layout.addLayout(parenthesis_layout)        
        """
        Backspace
        """
        backspace = MvgCalcInputButton(ActionKey.BACKSPACE.textSymbol)
        backspace.setStyleSheet(component_red("QPushButton")) 
        
        main_layout.addWidget(backspace) 
        backspace.clicked.connect(partial(self.handle_button_click, ActionKey.BACKSPACE))
        """
        D Pad
        """       
        d_pad = DPad()
        main_layout.addWidget(d_pad) 
        d_pad.button_click_signal_from_d_pad.connect(self.handle_button_click)

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_shared_keys.emit(key_type)