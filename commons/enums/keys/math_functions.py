from enum import Enum

class MathFunction(Enum):
    SQRT            = (1, "math.sqrt")
    SQUARED         = (2,"**2")
    CUBERT          = (3,"math.cbrt") #Will need a function for higher order roots and exponents
    CUBED           = (4,"**3")
    EXP             = (6,"**x")
    INVERSE         = (7,"**-1")
    LOG             = (8,"math.log")
    LOG_NATURAL     = (9,"math.ln")
    LOGTEN          = (10,"math.log10")
    FACTORIAL       = (11,"math.factorial")
    EXPONENTIAL2    = (12,"math.exp2")
    SIN             = (13,"math.sin")
    COS             = (14,"math.cos")
    TAN             = (15,"math.tan")
    INVSIN          = (16,"math.asin")
    INVCOS          = (17,"math.acos")
    INVTAN          = (18,"math.atan")
    SINH            = (19,"math.sinh")
    COSH            = (20,"math.cosh")
    TANH            = (21,"math.tanh")
