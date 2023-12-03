from io import StringIO
from typing import Optional
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont
from gui.enums.styles import COLORS
from gui.util.css import build_css_string
from lib.enums.base import BaseEnum, UnitEnum
from lib.enums.converter_enums import Measure

from lib.enums.keys import ActionKey
from lib.models.user_input import UserInput

from lib.util.constants import WINDOW_WIDTH
PRECISION  = 10

class MvgCalcExpressionTextField(QTextEdit):
    def __init__(self, parent = None):
        super().__init__(parent) 
        
        self.h_pos = None

        custom_font = QFont("roboto", 24)
        self.setFont(custom_font)
        self.setMinimumHeight(self.fontMetrics().height() * 2)
        self.setMaximumWidth(int(WINDOW_WIDTH) - 4)
        self.setReadOnly(True)

    def display_usr_inp_expr_as_str(self, user_input: UserInput, pos : int) -> str:

        try: 
            outputExprBuffer = StringIO()

            for index, key_input in enumerate(user_input.user_input_list):          
                if pos == index:
                    outputExprBuffer.write(f"<span style=")
                    outputExprBuffer.write(f"\"background-color: {COLORS.LIGHT_GREY.value};")
                    outputExprBuffer.write(f"color: {COLORS.WHITE.value};\">")
                    outputExprBuffer.write(key_input.textSymbol)
                    outputExprBuffer.write("</span>")
                else:   
                    outputExprBuffer.write(key_input.textSymbol)

            out_expr = outputExprBuffer.getvalue()

        finally:
            outputExprBuffer.close()

        return out_expr  

    def update(self, user_input : UserInput, action : Optional[ActionKey] = None) -> int:

        max_length = len(user_input.user_input_list)
        current_pos = max_length

        if isinstance(action, ActionKey):
            current_pos = self.set_current_pos(max_length, action)
            self.setText(self.display_usr_inp_expr_as_str(user_input, current_pos))
        else:
            self.setText(self.display_usr_inp_expr_as_str(user_input, -1))
            self.reset_pos()

        return current_pos
    
    #yes the unit converter code is in a QWidget for text formatting, it's lightweight
    def convert(self,user_input: UserInput, measure = BaseEnum, unit_1 = UnitEnum, unit_2 = UnitEnum):
        as_str = self.usr_inp_as_str(user_input)
        try:
            value_1 = float(as_str)

            if measure == Measure.LENGTH:
                result = value_1 * unit_1.ratio / unit_2.ratio
            elif measure == Measure.WEIGHT:
                result = value_1 * unit_2.ratio / unit_1.ratio
            
            #format string
            formatted_result = round(result,PRECISION)
            #print(formatted_result)
            self.setText(str(formatted_result).rstrip('0').rstrip('.'))
        except ValueError as e:
            pass
        
        #Weight value * self.unit_table[unit2] / self.unit_table[unit1]
        #length
        #result = value * self.unit_table[unit1] / self.unit_table[unit2]
    
    def set_current_pos(self, max_length : int, action : ActionKey) -> int:

        if self.h_pos is None: 
            self.h_pos = max_length + 1  
        
        if ActionKey.LEFT == action:
            if self.h_pos > 0:
                self.h_pos = self.h_pos - 1 
            if self.h_pos >= max_length:  
                self.h_pos = self.h_pos - 1
            return self.h_pos
        elif ActionKey.BACKSPACE == action:
            if self.h_pos > 0:
                self.h_pos = self.h_pos - 1 
            return self.h_pos
        elif ActionKey.RIGHT == action: 
            if self.h_pos < max_length:
                self.h_pos = self.h_pos + 1 
            return self.h_pos

    def reset_pos(self):
        self.h_pos = None
        
    def usr_inp_as_str(self, user_input: UserInput) -> str:

        """ Builds string from a list of user inputs formatted for evaluation 
            using pythons math library eval() function by default when display_to_user=False.
            If display_to_user indicator set to True then format and return a string that 
            is readable by the user

        Returns:
            String: formatted string
        """

        try: 
            outputExprBuffer = StringIO()

            for item in user_input.user_input_list:
                outputExprBuffer.write(item.textSymbol)
            out_expr = outputExprBuffer.getvalue()

        finally:
            outputExprBuffer.close()

        return out_expr 