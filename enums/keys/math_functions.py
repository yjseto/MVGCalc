from enum import Enum

class MathFunction(Enum):
    SIN      = 1
    COS      = 2
    TAN      = 3
    INVSIN   = 4
    INVCOS   = 5
    INVTAN   = 6
    SQRT     = 7
    SQUARED  = 8
    CUBERT   = 9
    CUBED    = 10
    EXP      = 11

class Operation(Enum):
    
    SIN        = MathFunction.SIN
    COS        = MathFunction.COS
    TAN        = MathFunction.TAN
    INVSIN     = MathFunction.INVSIN
    INVCOS     = MathFunction.INVCOS
    INVTAN     = MathFunction.INVTAN    

    def perform(self, x : any):
        if self == MathFunction.SIN:
            return ""
        elif self == MathFunction.COS:
            return ""
        elif self == MathFunction.TAN:
            return ""
        elif self == MathFunction.INVSIN:
            return ""
        elif self == MathFunction.INVCOS:
            return ""
        elif self == MathFunction.INVTAN:
            return ""