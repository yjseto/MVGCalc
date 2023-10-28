from enum import Enum

class DisplayMode(Enum):
    BASIC               = (0, "Calculator") #do we want to add (1,"evaluator_algebra.py") or something like that?
    GRAPH               = (1, "Graph")
    MENU                = (2, "Menu")
    # ALGEBRA             = (4, "") #solve algebraic equations and trigonometric identities
    # CALCULUS            = (5, "") #differentiation and integration
    # TIP_CALC            = (6, "")
    # EXPORT              = (7, "")
    def __init__ (self, index, textSymbol):
        self.index = index
        self.textSymbol = textSymbol  
        
class KeyboardDisplayMode(Enum):
    BASIC                   = (0, "Basic") #do we want to add (1,"evaluator_algebra.py") or something like that?
    FUNCTIONS               = (1, "Functions") #do we want to add (1,"evaluator_algebra.py") or something like that?
    def __init__ (self, index, textSymbol):
        self.index = index
        self.textSymbol = textSymbol  