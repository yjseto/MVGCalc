from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from io import StringIO
from gui.enums.styles import COLORS
from lib.enums.base import EvalEnum
from lib.enums.keys import CharacterInput, MathFunction, NumericInput, Operator
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr


@dataclass
class UserInput:
    
    user_input_list: list = field(default_factory=list)
    #result: str = field(default="")
    
    def get_user_input_list(self):
        return self.user_input_list
    


    def format_usr_inp_expr_as_str(self, display_to_user=False) -> str:

        """ Builds string from a list of user inputs formatted for evaluation 
            using pythons math library eval() function by default when display_to_user=False.
            If display_to_user indicator set to True then format and return a string that 
            is readable by the user

        Returns:
            String: formatted string
        """

        try: 
            outputExprBuffer = StringIO()
            counter = -1
            
            for item in self.user_input_list:
                # counts left and right parenthesis. If counter == 0 append base 10 as parameter
                counter = self.append_log_suffix(item, outputExprBuffer, display_to_user, counter)
                    
                outputExprBuffer.write(item.textSymbol if display_to_user else item.textEval)
            
            out_expr = outputExprBuffer.getvalue()

        finally:
            outputExprBuffer.close()

        return out_expr 
  
    
    def convert_usr_inp_exp_as_func(self):
        func = self.format_usr_inp_expr_as_str()
        parsed_expr = parse_expr(func,transformations='all')
        result = sp.sympify(parsed_expr)
        return result

    # def format_usr_inp_expr_as_latex(self) -> str:
    #     return f"idk this may be cool too one day"
    #i agree!

    def clear_list(self):
        self.user_input_list.clear()            

    def add_to_list(self, value, pos : Optional[int] = None):

        # block entering operator that require two operands at beginning of expression
        if self.is_empty() and (isinstance(value,Operator) or 
                                value == MathFunction.POW or 
                                value == MathFunction.SQUARED or
                                value == MathFunction.PERCENT):
            return
        
        # blocks numeric input if previous input was a %
        if self.get_prev() == MathFunction.PERCENT and (isinstance(value, CharacterInput) or isinstance(value, NumericInput)):
            return
        
        # merge two numeric inputs into single value.
        if isinstance(value, str) and isinstance(self.get_prev(),str): 
            value = self.get_prev() + value
            self.user_input_list.pop()
            self.user_input_list.append(value)
            return

        # replace operator
        if isinstance(self.get_prev(),Operator) and isinstance(value,Operator):
            self.user_input_list.pop()
            self.user_input_list.append(value)
        else:
            self.user_input_list.append(value) if pos is None else self.user_input_list.insert(pos, value)
            
            
    def remove_from_list(self, pos : Optional[int] = None):
        self.user_input_list.pop() if pos is None or pos >= len(self.user_input_list) else self.user_input_list.pop(pos)
    
    def get_prev(self):
        if not self.user_input_list:
            return
        return self.user_input_list[-1]
    
    def is_empty(self):
        return len(self.user_input_list) == 0
    
    # Evaluate Log to make sure the base is 10
    def append_log_suffix(self, item : EvalEnum, outputExprBuffer : StringIO, display_to_user : bool, counter : int) -> int:
        if counter > 0 and item == CharacterInput.LEFT_P:
            counter += 1
        
        if counter > 0 and item == CharacterInput.RIGHT_P:
            counter -= 1
        
        if counter == 0:
            counter = -1
            outputExprBuffer.write(CharacterInput.LOG_10_SUFFIX.textSymbol if display_to_user else CharacterInput.LOG_10_SUFFIX.textEval)

        
        if item == MathFunction.LOG:
            counter = 1
            
        return counter