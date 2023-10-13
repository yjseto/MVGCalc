from dataclasses import dataclass
from enum import Enum
from typing import List

@dataclass
class UserInput:
    #going to need to specify what type the unit is
    #probbaly using an Enum
    user_input: List[str | Enum] #what this class takes

    def format_to_float(self):
        out_expr = []
        for item in self.user_input:
            if isinstance(item, Enum): #if item is of type Enum, retrieve what is at said Enumeration
                self.output_expr.append(item.value[1])
            else:
                self.output_expr.append(str(item))
  
        out_expr = "".join(self.output_expr)

        return out_expr


