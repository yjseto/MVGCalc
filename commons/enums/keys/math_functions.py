from enum import Enum
import math

class MathFunction(Enum):
    SQRT            = (1, "math.sqrt")
    SQUARED         = (2,"**2")
    CUBERT          = (3,"math.cbrt") #Will need a function for higher order roots and exponents
    CUBED           = (4,"**3")
    POW             = (6,"math.pow")
    INVERSE         = (7,"**-1")
    LOG             = (8,"math.log") #customizable done by math.log(x,[,base]) 1 arugment ln(x)
    LOG_NATURAL     = (9,"math.ln")
    LOGTEN          = (10,"math.log10")
    FACTORIAL       = (11,"math.factorial") #x!
    EXPONENTIAL2    = (12,"math.exp2") #2^x
    EXP             = (13,"math.exp") #e^x
    ABSOLUTE_VAL    = (14,"math.fabs")
    MODULP          = (15,"math.modf") #float mod
    REMAINDER       = (16,"math.remainder") 
    GCD             = (17,"math.gcd")
    LCM             = (18,"math.lcm")
    TO_DEGREES      = (19,"math.degrees")
    TO_RADIANS      = (20,"math.radians")
    
    def retrieve(self):
        return self.value[1]