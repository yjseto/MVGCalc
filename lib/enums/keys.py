from lib.enums.base import EvalEnum, IconEnum

from gui.util.setup import *

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

class ActionKey(IconEnum):
    BACKSPACE       = (1, "del", None)
    UP              = (2, "", D_PAD_UP_ICON_FILE_PATH)
    DOWN            = (3, "", D_PAD_DOWN_ICON_FILE_PATH)
    RIGHT           = (4, "", D_PAD_RIGHT_ICON_FILE_PATH)
    LEFT            = (5, "", D_PAD_LEFT_ICON_FILE_PATH)
    CLEAR           = (6, "AC", None)
    ENTER           = (7, "=", None)   


class CharacterInput(EvalEnum):
    DECIMAL_POINT       = (1,"DECIMAL_POINT",      ".",    ".")
    LEFT_P              = (2,"LEFT_P",             "(",    "(")
    RIGHT_P             = (3,"RIGHT_P",            ")",    ")")
    NEGATIVE            = (4,"NEGITIVE",           "-",    "-")
    XVAR                = (5,"XVAR",               "x",    "X")
    YVAR                = (6,"YVAR",               "y",    "Y")
    ZVAR                = (7,"ZVAR",               "z",    "Z")
    LOG_10_SUFFIX       = (8,"LOG_10_SUFFIX",      ",10",   "")

class NumericInput(EvalEnum):
    ONE     = (1,   "ONE"   ,"1","1")
    TWO     = (2,   "TWO"   ,"2","2")
    THREE   = (3,   "THREE" ,"3","3")
    FOUR    = (4,   "FOUR"  ,"4","4")
    FIVE    = (5,   "FIVE"  ,"5","5")
    SIX     = (6,   "SIX"   ,"6","6")
    SEVEN   = (7,   "SEVEN" ,"7","7")    
    EIGHT   = (8,   "EIGHT" ,"8","8")
    NINE    = (9,   "NINE"  ,"9","9")      
    ZERO    = (10,  "ZERO"  ,"0","0") 

class MathFunction(EvalEnum):
    SQRT            = (1,"SQRT",                    "sqrt(",        "\u221A(")
    INVERSE         = (7,"INVERSE",                 "**-1",         "\u207B\u00B9")
    LOG             = (8,"LOG",                     "log(",         "log(") #customizable done by math.log(x,[,base]) 1 argument ln(x)
    LOG_NATURAL     = (9,"LOG_NATURAL",             "ln(",          "ln(")
    FACTORIAL       = (11,"FACTORIAL",              "math.factorial","") #x!
    EXP             = (13,"EXP",                    "math.exp",     "e^\u036F") #e^x
    ABSOLUTE_VAL    = (14,"ABSOLUTE_VAL",           "math.fabs",    "")
    MODULP          = (15,"MODULP",                 "math.modf",    "") #float mod
    REMAINDER       = (16,"REMAINDER",              "math.remainder","") 
    GCD             = (17,"GCD",                    "math.gcd",     "")
    LCM             = (18,"LCM",                    "math.lcm",     "")
    TO_DEGREES      = (19,"TO_DEGREES",             "math.degrees", "")
    TO_RADIANS      = (20,"TO_RADIANS",             "math.radians", "")
    POW             = (5,"POW",                     "**",     "^")
    SQUARED         = (6,"SQUARED",                 "**2",          "^2")
    # LOGTEN          = (10,"LOGTEN",                 "math.log10",   "")
    # EXPONENTIAL2    = (12,"EXPONENTIAL2",           "math.exp2",    "") #2^x
    # CUBERT          = (3,"CUBERT",                  "math.cbrt",    "") #Will need a function for higher order roots and exponents
    # CUBED           = (4,"CUBED",                   "**3",          "")
    PERCENT  = (21,"PERCENT",                "*0.01"       , "%")

class Operator(EvalEnum):
    ADD      = (1,"ADD",        "+",    "+")
    SUBTRACT = (2,"SUBTRACT",   "-",    "-")
    MULTIPLY = (3,"MULTIPLY",   "*",    "*")
    DIVIDE   = (4,"DIVIDE",     "/",    "/")#\u00F7
    #(^ on the calc) ** is eval() readable

        
# operation = Operation.ADD
# result = operation.perform(5, 3)

class TrigonometryFunction(EvalEnum):
    SIN         = (1,"SIN",     "sin(",         "sin(")
    COS         = (2,"COS",     "cos(",         "cos(")
    TAN         = (3,"TAN",     "tan(",         "tan(")
    INVSIN      = (4,"INVSIN",  "asin(",        "sin\u207B\u00B9(")
    INVCOS      = (5,"INVCOS",  "acos(",        "cos\u207B\u00B9(")
    INVTAN      = (6,"INVTAN",  "atan(",        "tan\u207B\u00B9(")

class MathConstants(EvalEnum):
    PI          = (1,"","pi","\u03C0")
    EULERSNUM   = (2,"","E","e")
