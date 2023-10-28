import math
from enum import Enum

class MathConstants(Enum):
    PI          = (1,"","pi","\u03C0")
    EULERSNUM   = (2,"","e","e")
    # TAU         = (3,"math.tau")
    # INFINITY    = (4,"math.inf")
    # NAN         = (5,"math.nan")

    def __init__ (self, index, textId, textEval, textSymbol):
        self.index = index
        self.textId = textId
        self.textEval = textEval
        self.textSymbol = textSymbol