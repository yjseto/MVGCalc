from dataclasses import dataclass, field
from enum import Enum
from typing import List
from io import StringIO

@dataclass
class UserInput:
    
    user_input_list: list = field(default_factory=list)
    current_numeric_input: str = field(default="")

    # output_expr: List [str] #good to hold onto in the class object for splicing equations together
    # #takes an output expr list as a string
    # def format_usr_inp_expr_as_str(self) -> str:
    #     for item in self.user_input:
    #         if isinstance(item, Enum): #if item is of type Enum, retrieve what is at said Enumeration
    #             self.output_expr.append(item.value[1])
    #         else:
    #             self.output_expr.append(str(item))
  
    #     out_expr = "".join(self.output_expr)

    #     return out_expr
    

    def format_usr_inp_expr_as_str(self) -> str:

        """ Builds string from a list of user inputs specifically 
            formatted for evaluation using pythons math library eval() function.

        Returns:
            String: formatted string
        """

        try: 
            outputExprBuffer = StringIO()

            for item in self.user_input_list:

                #if item is of type Enum append textEval property value
                if isinstance(item, Enum): 
                    outputExprBuffer.write(item.textEval)
                else:
                    outputExprBuffer.write(str(item))
    
            out_expr = outputExprBuffer.getvalue()

        finally:
            outputExprBuffer.close()

        return out_expr    


    # def format_usr_inp_expr_as_latex(self) -> str:
    #     return f"idk this may be cool too one day"
    #i agree!

    #lets not use this now
    def validate_user_input(self) -> bool: 
        operand_count = 0
        for item in self.user_input_list:
            if isinstance(item, Enum):
                operand_count += 1
            else:
                operand_count = 0

            if operand_count == 2:
                return False
        return True
         
                




    