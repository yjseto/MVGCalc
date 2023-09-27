from dataclasses import dataclass
from enum import Enum
from typing import List
#from ..enums.keys import operators,character_inputs,math_functions

@dataclass
class UserInput:
    user_input: List[str | Enum]
    output_expr: List [str] #good to hold onto in the class object for splicing equations together
    #takes an output expr list as a string
    def format_usr_inp_expr_as_str(self) -> str:
        for item in self.user_input:
            if isinstance(item, Enum): #if item is of type Enum, retrieve what is at said Enumeration
                self.output_expr.append(item.retrieve())
            else:
                self.output_expr.append(str(item))
  
        out_expr = "".join(self.output_expr)

        return out_expr


    

    # def format_usr_inp_expr_as_latex(self) -> str:
    #     return f"idk this may be cool too one day"
    #i agree!



    