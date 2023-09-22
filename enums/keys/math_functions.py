from enum import Enum
import math

class MathFunction(Enum):
    SIN      = (1,"math.sin()")
    COS      = (2,"math.cos()")
    TAN      = (3,"math.tan()")
    INVSIN   = (4,"math.asin()")
    INVCOS   = (5,"math.acos()")
    INVTAN   = (6,"math.atan()")
    SQRT     = (7, "math.sqrt()")
    SQUARED  = (8,"**2")
    CUBERT   = (9) #Will need a function for higher order roots and exponents
    CUBED    = (10,"**3")
    EXP      = (11,"**x")
    INVERSE  = (12,"**-1")
