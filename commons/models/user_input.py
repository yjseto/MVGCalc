from dataclasses import dataclass
from enum import Enum
from typing import List

@dataclass
class UserInput:
    user_input: List[str | Enum]
    operation: int
    variable: str

    def format_usr_inp_expr_as_str(self) -> str:
        return f"Do stuff to turn the user_input list into a valid string expression"
    

    # def format_usr_inp_expr_as_latex(self) -> str:
    #     return f"idk this may be cool too one day"



    