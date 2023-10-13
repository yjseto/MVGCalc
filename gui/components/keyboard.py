from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect

from gui.components.button import MvgCalcKeyButton, EnterButton, ClearInputButton, PercentButton
from lib.enums.keys import *
from lib.models.user_input import UserInput

class BasicKeyboard(QWidget):
    def __init__(self, _user_input : UserInput):
        super().__init__()
        
        
        grid = QGridLayout()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIRST ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        clear = ClearInputButton(
             ActionKey.CLEAR.textSymbol,        # character displayed on button
             ActionKey.CLEAR,                   # value added to array
             _user_input,                       # user input array
             QRect(277, 351, 83, 79),           # button dimensions
             self)                                              

        grid.addWidget(clear,0,0)

        parethesis = MvgCalcKeyButton(
             CharacterInput.LEFT_P.textSymbol + CharacterInput.RIGHT_P.textSymbol,       
             CharacterInput.LEFT_P,                  
             _user_input,                     
             QRect(277, 351, 83, 79),         
             self)                                              

        grid.addWidget(parethesis,0,1)        

        #need to add to enum
        percent = PercentButton(
             "%",       
             CharacterInput.LEFT_P,                  
             _user_input,                     
             QRect(277, 351, 83, 79),         
             self)                                              

        grid.addWidget(percent,0,2)          
        
        division = MvgCalcKeyButton(
             Operator.DIVIDE.textSymbol,        
             Operator.DIVIDE,                   
             _user_input,                       
             QRect(277, 351, 83, 79),           
             self)                                              

        grid.addWidget(division,0,3)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        SECOND ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        seven = MvgCalcKeyButton(
             "7",                               
             "7",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(seven,1,0)

        eight = MvgCalcKeyButton(
             "8",                               
             "8",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(eight,1,1)        

        nine = MvgCalcKeyButton(
             "9",                               
             "9",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(nine,1,2) 

        multiplication = MvgCalcKeyButton(
             Operator.MULTIPLY.textSymbol,      
             Operator.MULTIPLY,                 
             _user_input,                       
             QRect(277, 351, 83, 79),           
             self)   

        grid.addWidget(multiplication,1,3)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
           THIRD ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        four = MvgCalcKeyButton(
             "4",                               
             "4",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(four,2,0)

        five = MvgCalcKeyButton(
             "5",                               
             "5",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(five,2,1)        

        six = MvgCalcKeyButton(
             "6",                               
             "6",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(six,2,2) 

        subtract = MvgCalcKeyButton(
             Operator.SUBTRACT.textSymbol,      
             Operator.SUBTRACT,                 
             _user_input,                       
             QRect(277, 351, 83, 79),           
             self)   

        grid.addWidget(subtract,2,3)        

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FOURTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        one = MvgCalcKeyButton(
             "1",                               
             "1",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(one,3,0)

        two = MvgCalcKeyButton(
             "2",                               
             "2",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(two,3,1)        

        three = MvgCalcKeyButton(
             "3",                               
             "3",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(three,3,2) 

        subtract = MvgCalcKeyButton(
             Operator.ADD.textSymbol,      
             Operator.ADD,                 
             _user_input,                       
             QRect(277, 351, 83, 79),           
             self)   

        grid.addWidget(subtract,3,3)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        FIFTH ROW
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        negitive = MvgCalcKeyButton(
             CharacterInput.NEGATIVE.textSymbol,                               
             CharacterInput.NEGATIVE,                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(negitive,4,0)

        zero = MvgCalcKeyButton(
             "0",                               
             "0",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(zero,4,1)        

        decimal_point = MvgCalcKeyButton(
             ".",                               
             ".",                       
             _user_input,                       
             QRect(277, 351, 83, 79),          
             self)   

        grid.addWidget(decimal_point,4,2) 

        enter = EnterButton(
             ActionKey.ENTER.textSymbol,      
             ActionKey.ENTER,                 
             _user_input,                       
             QRect(277, 351, 83, 79),           
             self)   

        grid.addWidget(enter,4,3)

        self.setLayout(grid)