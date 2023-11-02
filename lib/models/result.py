from dataclasses import dataclass, field

import numpy as np
from typing import Protocol

class IResult(Protocol):
    error_msgs: [str]
    success: bool
    value: any
    expression : str
    #add value and expression in the future?


# A structural subtype of IShape
# Not a nominal subtype of IShape

class BasicResult(IResult):
    def __init__(self):
        self.value : str = ""
        self.error_msgs = []
        self.success = False
        self.expression: str = ""

class GraphResult(IResult):
    def __init__(self):
        self.value : str
        self.error_msgs = []
        self.success = False
        self.expression: str = ""
        #self.clear_graph == False
        self.y: str
        self.trig_func = False

'''
@dataclass
class GraphResult(ResultBase):
    result = "?"

@dataclass
class CalculusResult(ResultBase):
     result = ""

@dataclass
class CalculusResult(ResultBase):
     result = "? we may want to return two results for each side of the conversion"

'''     