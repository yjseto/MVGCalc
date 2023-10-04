from enum import Enum

'''
README

This file contains enumerations for key inputs from the calculator.
To evaluate an expression, the function format_usr_inp_expr_as_str in user_input.py in commons/models
takes a user input as a list, in the list objects of enumeration are accepted/expected.

To know what values/properties/names belong to an enumeration, one can do the following:
An enumeration has a name and a value.  
For example, take the character input class
An object of this class, could be XVAR
say we come across an XVAR object and its called item as it is in the format_usr_inp_expr_as_str function
we can get the name of it by saying item.name
we can get the value of it by item.value
we can get the string representation as item.value[1] which is how I get it to be formatted in an eval() readable string
these calues are able to be called without any __init__ function

Please see how to do output in unit_tests.py

'''


class ActionKey(Enum):
    BACKSPACE       = 1
    UP              = 2
    DOWN            = 3
    RIGHT           = 4
    LEFT            = 5
    CLEAR           = 6
    ENTER           = 7
    #MODE?
    
    def retrieve(self):
        return self.value[1]
    
class CharacterInput(Enum):
    XVAR                = (1,"x")
    DECIMAL             = (2,".")
    LEFT_P              = (3,"(")
    RIGHT_P             = (4,")")
    NEGATIVE            = (5,"-")
    YVAR                = (6,"y")
    ZVAR                = (7,"z")

    #object.name = XVAR, DECIMAL, ETC.
    #object.value = 1,2,3,4
    #object.value[1] = "x",".""()"etc..
    

    def retrieve(self):
        return self.value[1]
    

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

class Operator(Enum):
    ADD      = (1,"+")
    SUBTRACT = (2,"-")
    MULTIPLY = (3,"*")
    DIVIDE   = (4,"/")
    #(^ on the calc) ** is eval() readable
    EXPONENT = (5,"**")
    
    def retrieve(self):
        return self.value[1]
        
        #Think we're going to change this function
        
# operation = Operation.ADD
# result = operation.perform(5, 3)

class Trigonometry(Enum):
    SIN         = (1,"math.sin")
    COS         = (2,"math.cos")
    TAN         = (3,"math.tan")
    INVSIN      = (4,"math.asin")
    INVCOS      = (5,"math.acos")
    INVTAN      = (6,"math.atan")
    SINH        = (7,"math.sinh") #Hyperbolic functions
    COSH        = (8,"math.cosh")
    TANH        = (9,"math.tanh")

    def retrieve(self):
        return self.value[1]

class SympyTrig(Enum): #this class allows the sympy evaluator to read trig functions
    SIN         = (1,"sin")
    COS         = (2,"cos")
    TAN         = (3,"tan")
    INVSIN      = (4,"asin")
    INVCOS      = (5,"acos")
    INVTAN      = (6,"atan")
    SINH        = (7,"sinh") #Hyperbolic functions
    COSH        = (8,"cosh")
    TANH        = (9,"tanh")