from dataclasses import dataclass, field
from enum import Enum
from typing import List
from io import StringIO
from lib.enums.keys import Operator
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, transformations

@dataclass
class UserInput:
    
    user_input_list: list = field(default_factory=list)
    result: str = field(default="")
    update_graph_flag = False

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

            for item in self.user_input_list:

                if isinstance(item, Enum): 
                    outputExprBuffer.write(item.textSymbol if display_to_user else item.textEval)
                else:
                    outputExprBuffer.write(str(item))
    
            out_expr = outputExprBuffer.getvalue()

        finally:
            outputExprBuffer.close()

        return out_expr    
    
    def convert_usr_inp_exp_as_func(self):
        func = self.format_usr_inp_expr_as_str()
        parsed_expr = parse_expr(func,transformations='all')
        result = sp.sympify(parsed_expr)
        return result
    
    def update_graph(self,expression):
        '''
        work in progress, not sure how to write this yet
        but the idea is to let the graphDisplay wdiget that we are ready to plot something
        '''
        if self.update_graph_flag == False:
            self.update_graph_flag = True
        self.update_graph_flag = False
        pass

    # def format_usr_inp_expr_as_latex(self) -> str:
    #     return f"idk this may be cool too one day"
    #i agree!

    def clear_result(self):
        self.result = ""

    def clear_list(self):
        self.user_input_list.clear()            

    def add_to_list(self,value):
        if not self.user_input_list and isinstance(value,Operator):
            return
        
        if isinstance(value, str) and isinstance(self.get_prev(),str): 
            value = self.get_prev() + value
            self.user_input_list.pop()
            self.user_input_list.append(value)
            return

        if isinstance(self.get_prev(),Operator) and isinstance(value,Operator):
            self.user_input_list.pop()
            self.user_input_list.append(value)
        else:
            self.user_input_list.append(value)
        
    def pop_from_list(self):
        self.user_input_list.pop()
    
    def get_prev(self):
        if not self.user_input_list:
            return
        return self.user_input_list[-1]