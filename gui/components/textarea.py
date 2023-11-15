from io import StringIO
from typing import Optional
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont
from gui.enums.styles import COLORS
from gui.util.css import build_css_string

from lib.enums.keys import ActionKey
from lib.models.user_input import UserInput

from lib.util.constants import WINDOW_WIDTH

class MvgCalcExpressionTextField(QTextEdit):
    def __init__(self, parent = None):
        super().__init__(parent) 
        
        self.h_pos = None


        self.setMinimumHeight(self.fontMetrics().height() * 2)
        self.setMaximumWidth(int(WINDOW_WIDTH) - 4)
        self.setReadOnly(True)
        
        self.setStyleSheet(build_css_string(
            "QTextEdit",
            background_color= "#20252E",
            color= "#CBE1FF",
            font_size="24pt"
            ))

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
        
        