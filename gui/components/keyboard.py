import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from gui.components.listbox import HistoricExpressionListWidget

from lib.enums.keys import *
from lib.util.constants import *
from lib.enums.modes import *

from gui.components.button import MvgCalcInputButton, MvgCalcHalfInputButton, MvgCalcInputButton, MvgCalcInputButton2
from gui.util.css import *
from gui.util.setup import *

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
        seven = MvgCalcInputButton2(NumericInput.SEVEN.textSymbol, width_input_multiplier, height_input_multiplier, self)   
        seven.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(seven)
        seven.clicked.connect(partial(self.handle_button_click, NumericInput.SEVEN))
        
        """
        Eight 8
        """
        eight = MvgCalcInputButton2(NumericInput.EIGHT.textSymbol,width_input_multiplier, height_input_multiplier, self)   
        eight.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(eight)        
        eight.clicked.connect(partial(self.handle_button_click, NumericInput.EIGHT))
        """
        Nine 9
        """
        nine = MvgCalcInputButton2(NumericInput.NINE.textSymbol,width_input_multiplier, height_input_multiplier, self) 
        nine.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(nine) 
        nine.clicked.connect(partial(self.handle_button_click, NumericInput.NINE))    
        """
        Square Root
        """
        sqrt = MvgCalcInputButton2(MathFunction.SQRT.get_no_parentheses(),width_input_multiplier, height_input_multiplier, self)
        sqrt.setStyleSheet(component_blue("QPushButton"))   
        
        row2.addWidget(sqrt) 
        sqrt.clicked.connect(partial(self.handle_button_click, MathFunction.SQRT))   
        """
        Percent %  
        """
        percent = MvgCalcInputButton2(MathFunction.PERCENT.textSymbol, width_input_multiplier, height_input_multiplier, self)  
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
        four = MvgCalcInputButton2(NumericInput.FOUR.textSymbol, width_input_multiplier, height_input_multiplier, self)   
        four.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(four)
        four.clicked.connect(partial(self.handle_button_click, NumericInput.FOUR))
        """
        Five 5
        """
        five = MvgCalcInputButton2(NumericInput.FIVE.textSymbol, width_input_multiplier, height_input_multiplier, self)   
        five.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(five)   
        five.clicked.connect(partial(self.handle_button_click, NumericInput.FIVE))
        """
        Six 6
        """
        six = MvgCalcInputButton2(NumericInput.SIX.textSymbol, width_input_multiplier, height_input_multiplier, self)  
        six.setStyleSheet(component_dark_grey("QPushButton"))
          
        row3.addWidget(six) 
        six.clicked.connect(partial(self.handle_button_click, NumericInput.SIX))
        """
        Squared
        """
        squared = MvgCalcInputButton2("x\u00b2", width_input_multiplier, height_input_multiplier, self)   
        squared.setStyleSheet(component_blue("QPushButton"))

        row3.addWidget(squared)        
        squared.clicked.connect(partial(self.handle_button_click, MathFunction.SQUARED))
        """
        Division
        """
        division = MvgCalcInputButton2(Operator.DIVIDE.textSymbol,width_input_multiplier, height_input_multiplier, self)                                              
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
        one = MvgCalcInputButton2(NumericInput.ONE.textSymbol, width_input_multiplier, height_input_multiplier,self)   
        one.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(one)  
        one.clicked.connect(partial(self.handle_button_click, NumericInput.ONE))
        """
        Two 2
        """  
        two = MvgCalcInputButton2(NumericInput.TWO.textSymbol, width_input_multiplier, height_input_multiplier, self)   
        two.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(two)       
        two.clicked.connect(partial(self.handle_button_click, NumericInput.TWO))
        """
        Three 3
        """  
        three = MvgCalcInputButton2(NumericInput.THREE.textSymbol, width_input_multiplier, height_input_multiplier, self) 
        three.setStyleSheet(component_dark_grey("QPushButton"))
          
        row4.addWidget(three)    
        three.clicked.connect(partial(self.handle_button_click, NumericInput.THREE))
        """
        Add +
        """  
        add = MvgCalcInputButton2(Operator.ADD.textSymbol, width_input_multiplier, height_input_multiplier, self)   
        add.setStyleSheet(component_blue("QPushButton"))
        
        row4.addWidget(add)    
        add.clicked.connect(partial(self.handle_button_click, Operator.ADD))
        """
        Multiply
        """  
        multiplication = MvgCalcInputButton2(Operator.MULTIPLY.textSymbol, width_input_multiplier, height_input_multiplier, self)  
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
        negitive = MvgCalcInputButton2("\u207A\u2215\u208B", width_input_multiplier, height_input_multiplier,self)
        negitive.setStyleSheet(component_light_grey("QPushButton", border_bottom_left_radius = "8px"))
        
        row5.addWidget(negitive)
        negitive.clicked.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcInputButton2(NumericInput.ZERO.textSymbol,width_input_multiplier, height_input_multiplier, self)
        zero.setStyleSheet(component_dark_grey("QPushButton"))
           
        row5.addWidget(zero)        
        zero.clicked.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcInputButton2(CharacterInput.DECIMAL_POINT.textSymbol, width_input_multiplier, height_input_multiplier, self)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.clicked.connect(partial(self.handle_button_click, CharacterInput.DECIMAL_POINT))
        """
        Subtract -
        """ 
        subtract = MvgCalcInputButton2(Operator.SUBTRACT.textSymbol,width_input_multiplier, height_input_multiplier, self)   
        subtract.setStyleSheet(component_blue("QPushButton"))

        row5.addWidget(subtract)          
        subtract.clicked.connect(partial(self.handle_button_click, Operator.SUBTRACT))
        """
        Enter
        """         
        enter = MvgCalcInputButton2(ActionKey.ENTER.textSymbol, width_input_multiplier, height_input_multiplier, self)   
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
        sin = MvgCalcInputButton2(TrigonometryFunction.SIN.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        sin.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(sin)
        sin.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.SIN))
        """
        Cos 
        """ 
        cos = MvgCalcInputButton2(TrigonometryFunction.COS.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        cos.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(cos)
        cos.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.COS))
        """
        Tan
        """ 
        tan = MvgCalcInputButton2(TrigonometryFunction.TAN.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        tan.setStyleSheet(component_dark_grey("QPushButton"))
        
        row2.addWidget(tan)
        tan.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.TAN))
        """
        X
        """          
        x_var = MvgCalcInputButton2(CharacterInput.XVAR.textSymbol, width_function_multiplier, height_function_multiplier, self)
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
        invsin = MvgCalcInputButton2(TrigonometryFunction.INVSIN.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        invsin.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invsin)
        invsin.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.INVSIN))
        """
        Cos Inv 
        """ 
        invcos = MvgCalcInputButton2(TrigonometryFunction.INVCOS.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        invcos.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invcos)
        invcos.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.INVCOS))
        """
        Tan Inv
        """ 
        invtan = MvgCalcInputButton2(TrigonometryFunction.INVTAN.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        invtan.setStyleSheet(component_dark_grey("QPushButton"))
        
        row3.addWidget(invtan)
        invtan.clicked.connect(partial(self.handle_button_click, TrigonometryFunction.INVTAN))
        """
        Pi
        """          
        pi = MvgCalcInputButton2(MathConstants.PI.textSymbol, width_function_multiplier, height_function_multiplier, self)
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
        log = MvgCalcInputButton2(MathFunction.LOG.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        log.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(log)
        log.clicked.connect(partial(self.handle_button_click, MathFunction.LOG))
        """
        Natural Log
        """ 
        nat_log = MvgCalcInputButton2(MathFunction.LOG_NATURAL.get_no_parentheses(), width_function_multiplier, height_function_multiplier, self)   
        nat_log.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(nat_log)
        nat_log.clicked.connect(partial(self.handle_button_click, MathFunction.LOG_NATURAL))
        """
        Pow 10
        """ 
        power = MvgCalcInputButton2(MathFunction.POW.textSymbol, width_function_multiplier, height_function_multiplier, self)   
        power.setStyleSheet(component_dark_grey("QPushButton"))
        
        row4.addWidget(power)
        power.clicked.connect(partial(self.handle_button_click, MathFunction.POW))
        """
        Eulers #
        """          
        e = MvgCalcInputButton2(MathConstants.EULERSNUM.textSymbol, width_function_multiplier, height_function_multiplier, self)
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
        negitive = MvgCalcInputButton2("\u207A\u2215\u208B", width_function_multiplier, height_function_multiplier, self)  
        negitive.setStyleSheet(component_light_grey("QPushButton"))
        
        row5.addWidget(negitive)
        negitive.clicked.connect(partial(self.handle_button_click, CharacterInput.NEGATIVE))
        """
        Zero 0
        """          
        zero = MvgCalcInputButton2(NumericInput.ZERO.textSymbol, width_function_multiplier, height_function_multiplier, self)
        zero.setStyleSheet(component_blue("QPushButton"))
           
        row5.addWidget(zero)        
        zero.clicked.connect(partial(self.handle_button_click, NumericInput.ZERO))
        """
        Decimal Point .
        """ 
        decimal_point = MvgCalcInputButton2(CharacterInput.DECIMAL_POINT.textSymbol, width_function_multiplier, height_function_multiplier, self)   
        decimal_point.setStyleSheet(component_dark_grey("QPushButton"))
        
        row5.addWidget(decimal_point)   
        decimal_point.clicked.connect(partial(self.handle_button_click, CharacterInput.DECIMAL_POINT))
        """
        Enter
        """         
        enter = MvgCalcInputButton2(ActionKey.ENTER.textSymbol, width_function_multiplier, height_function_multiplier, self)   
        enter.setStyleSheet(component_blue("QPushButton",border_bottom_right_radius = "8px"))
        
        row5.addWidget(enter)   
        enter.clicked.connect(partial(self.handle_button_click, ActionKey.ENTER)) 

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_keyboard.emit(key_type)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HISTORIC EXPRESSION KEYS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class HistoricExpressionKeyboard(QWidget):

    button_click_signal_from_keyboard = pyqtSignal(BaseEnum)

    def __init__(self, display_mode : DisplayMode, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.display_mode = display_mode

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW - Shared Keys
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""     
        shared_keys = SharedKeyRow()
        main_layout.addWidget(shared_keys) 
        shared_keys.button_click_signal_from_shared_keys.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Historic Expression Listbox
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""          
        self.hist_expr_listbox = HistoricExpressionListWidget(display_mode)
        main_layout.addWidget(self.hist_expr_listbox) 

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

        horizontal_layout_up = QHBoxLayout()
        horizontal_layout_up.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        up_arrow = MvgCalcInputButton2(ActionKey.UP.textSymbol, width_input_multiplier * 0.65, height_input_multiplier * 0.4, self)  
        up_arrow.setIcon(QtGui.QIcon(ActionKey.UP.iconPath))
        up_arrow.setIconSize(QtCore.QSize(50, 50))
        up_arrow.setStyleSheet(component_black("QPushButton"))
        up_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.UP))

        horizontal_layout_up.addWidget(up_arrow)
        main_layout.addLayout(horizontal_layout_up)
    
        horizontal_layout = QHBoxLayout()
        
        left_arrow = MvgCalcInputButton2(ActionKey.LEFT.textSymbol, width_input_multiplier * 0.4, height_input_multiplier * 0.65, self)
        left_arrow.setIcon(QtGui.QIcon(ActionKey.LEFT.iconPath))
        left_arrow.setIconSize(QtCore.QSize(50, 50))
        left_arrow.setStyleSheet(component_black("QPushButton"))  
        left_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.LEFT))

        horizontal_layout.addWidget(left_arrow)
        spaceItem = QSpacerItem(40, 0, hPolicy=QSizePolicy.Policy.Minimum, vPolicy=QSizePolicy.Policy.Minimum)
        horizontal_layout.addSpacerItem(spaceItem)
        
        right_arrow = MvgCalcInputButton2(ActionKey.RIGHT.textSymbol, width_input_multiplier * 0.4, height_input_multiplier *0.65, self)
        right_arrow.setIcon(QtGui.QIcon(ActionKey.RIGHT.iconPath))
        right_arrow.setIconSize(QtCore.QSize(50, 50))
        right_arrow.setStyleSheet(component_black("QPushButton"))  
        right_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.RIGHT))

        horizontal_layout.addWidget(right_arrow)
        main_layout.addLayout(horizontal_layout)
        
        horizontal_layout_down = QHBoxLayout()
        horizontal_layout_down.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        down_arrow = MvgCalcInputButton2(ActionKey.DOWN.textSymbol, width_input_multiplier *0.65, height_input_multiplier * 0.4, self)
        down_arrow.setIcon(QtGui.QIcon(ActionKey.DOWN.iconPath))  
        down_arrow.setIconSize(QtCore.QSize(50, 50))
        down_arrow.setStyleSheet(component_black("QPushButton"))
        down_arrow.clicked.connect(partial(self.handle_button_click, ActionKey.DOWN))

        horizontal_layout_down.addWidget(down_arrow)
        main_layout.addLayout(horizontal_layout_down)

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
        main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(main_layout)
        """
        Clear Button
        """
        clear = MvgCalcInputButton2(ActionKey.CLEAR.textSymbol, width_input_multiplier, height_input_multiplier) 
        clear.setStyleSheet(component_light_grey("QPushButton", border_top_left_radius = "8px",max_width = "20px"))
        main_layout.addWidget(clear)
        clear.clicked.connect(
            partial(self.handle_button_click, ActionKey.CLEAR))       
        """
        Left Parenthesis
        """
        left_parethesis = MvgCalcHalfInputButton(CharacterInput.LEFT_P.textSymbol, width_input_multiplier*0.45, height_input_multiplier, self)             
        left_parethesis.setStyleSheet(component_light_grey("QPushButton"))
        
        left_parethesis.clicked.connect(
            partial(self.handle_button_click, CharacterInput.LEFT_P))
        """
        Right Parenthesis
        """
        right_parethesis = MvgCalcHalfInputButton(CharacterInput.RIGHT_P.textSymbol, width_input_multiplier*0.45, height_input_multiplier, self)                                                   
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
        
        spaceItem = QSpacerItem(10, 20, hPolicy=QSizePolicy.Policy.Maximum, vPolicy=QSizePolicy.Policy.Minimum)
        main_layout.addSpacerItem(spaceItem)
        """
        D Pad
        """       
        d_pad = DPad()
        d_pad.setContentsMargins(0,0,10,0)
        main_layout.addWidget(d_pad) 
        d_pad.button_click_signal_from_d_pad.connect(self.handle_button_click)

    def handle_button_click(self, key_type : BaseEnum):
        self.button_click_signal_from_shared_keys.emit(key_type)