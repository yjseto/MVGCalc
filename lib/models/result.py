from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from lib.models.user_input import UserInput

class ResultBase(ABC):

    error_msg: str = field(default="")
    success: bool
    
    def clean_up(self, user_input : UserInput):
            user_input.clear_list

@dataclass
class ArithmeticResult(ResultBase):
    result = "" 

@dataclass
class GraphResult(ResultBase):
    result = "?"

@dataclass
class CalculusResult(ResultBase):
     result = ""

@dataclass
class CalculusResult(ResultBase):
     result = "? we may want to return two results for each side of the conversion"