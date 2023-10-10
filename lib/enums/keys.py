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

    #object.name = XVAR, DECIMAL, ETC.
    #object.value = 1,2,3,4
    #object.value[1] = "x",".""()"etc..

class ActionKey(Enum):
    BACKSPACE       = (1, "")
    UP              = (2, "")
    DOWN            = (3, "")
    RIGHT           = (4, "")
    LEFT            = (5, "")
    CLEAR           = (6, "AC")
    ENTER           = (7, "=")

    def __init__ (self, index, textSymbol):
        self.index = index
        self.textSymbol = textSymbol        
    
class CharacterInput(Enum):
    DECIMAL_POINT       = (1,"DECIMAL_POINT",      ".",    ".")
    LEFT_P              = (2,"LEFT_P",             "(",    "(")
    RIGHT_P             = (3,"RIGHT_P",            ")",    ")")
    NEGATIVE            = (4,"NEGITIVE",           "-",    "-")
    XVAR                = (5,"XVAR",               "x",    "X")
    YVAR                = (6,"YVAR",               "y",    "Y")
    ZVAR                = (7,"ZVAR",               "z",    "Z")

    
    def __init__ (self, index, textId, textEval, textSymbol):
        self.index = index
        self.textId = textId
        self.textEval = textEval
        self.textSymbol = textSymbol
    

class MathFunction(Enum):
    SQRT            = (1,"SQRT",                    "math.sqrt",    "")
    SQUARED         = (2,"SQUARED",                 "**2",          "")
    CUBERT          = (3,"CUBERT",                  "math.cbrt",    "") #Will need a function for higher order roots and exponents
    CUBED           = (4,"CUBED",                   "**3",          "")
    POW             = (6,"POW",                     "math.pow",     "")
    INVERSE         = (7,"INVERSE",                 "**-1",         "")
    LOG             = (8,"LOG",                     "math.log",     "") #customizable done by math.log(x,[,base]) 1 arugment ln(x)
    LOG_NATURAL     = (9,"LOG_NATURAL",             "math.ln",      "")
    LOGTEN          = (10,"LOGTEN",                 "math.log10",   "")
    FACTORIAL       = (11,"FACTORIAL",              "math.factorial","") #x!
    EXPONENTIAL2    = (12,"EXPONENTIAL2",           "math.exp2",    "") #2^x
    EXP             = (13,"EXP",                    "math.exp",     "") #e^x
    ABSOLUTE_VAL    = (14,"ABSOLUTE_VAL",           "math.fabs",    "")
    MODULP          = (15,"MODULP",                 "math.modf",    "") #float mod
    REMAINDER       = (16,"REMAINDER",              "math.remainder","") 
    GCD             = (17,"GCD",                    "math.gcd",     "")
    LCM             = (18,"LCM",                    "math.lcm",     "")
    TO_DEGREES      = (19,"TO_DEGREES",             "math.degrees", "")
    TO_RADIANS      = (20,"TO_RADIANS",             "math.radians", "")
    
    def __init__ (self, index, textId, textEval, textSymbol):
        self.index = index
        self.textId = textId
        self.textEval = textEval
        self.textSymbol = textSymbol

class Operator(Enum):
    ADD      = (1,"ADD",        "+",    "+")
    SUBTRACT = (2,"SUBTRACT",   "-",    "-")
    MULTIPLY = (3,"MULTIPLY",   "*",    "x")
    DIVIDE   = (4,"DIVIDE",     "/",    "\u00F7")
    #(^ on the calc) ** is eval() readable
    EXPONENT = (5,"EXPONENT",   "**",   "")
    
    def __init__ (self, index, textId, textEval, textSymbol):
        self.index = index
        self.textId = textId
        self.textEval = textEval
        self.textSymbol = textSymbol
        
# operation = Operation.ADD
# result = operation.perform(5, 3)

class Trigonometry(Enum):
    SIN         = (1,"SIN",     "math.sin",     "")
    COS         = (2,"COS",     "math.cos",     "")
    TAN         = (3,"TAN",     "math.tan",     "")
    INVSIN      = (4,"INVSIN",  "math.asin",    "")
    INVCOS      = (5,"INVCOS",  "math.acos",    "")
    INVTAN      = (6,"INVTAN",  "math.atan",    "")
    SINH        = (7,"SINH",    "math.sinh",    "") #Hyperbolic functions
    COSH        = (8,"COSH",    "math.cosh",    "")
    TANH        = (9,"TANH",    "math.tanh",    "")

    def __init__ (self, index, textId, textEval, textSymbol):
        self.index = index
        self.textId = textId
        self.textEval = textEval
        self.textSymbol = textSymbol

class SympyTrig(Enum): #this class allows the sympy evaluator to read trig functions
    SIN         = (1,"SYMPY_SIN",     "sin","")
    COS         = (2,"SYMPY_COS",     "cos","")
    TAN         = (3,"SYMPY_TAN",     "tan","")
    INVSIN      = (4,"SYMPY_INVSIN",  "asin","")
    INVCOS      = (5,"SYMPY_INVCOS",  "acos","")
    INVTAN      = (6,"SYMPY_INVTAN",  "atan","")
    SINH        = (7,"SYMPY_SINH",    "sinh","") #Hyperbolic functions
    COSH        = (8,"SYMPY_COSH",    "cosh","")
    TANH        = (9,"SYMPY_TANH",    "tanh","")

    def __init__ (self, index, textId, textEval, textSymbol):
        self.index = index
        self.textId = textId
        self.textEval = textEval
        self.textSymbol = textSymbol