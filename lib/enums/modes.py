from lib.enums.base import BaseEnum

class DisplayMode(BaseEnum):
    BASIC               = (0, "Calculator") #do we want to add (1,"evaluator_algebra.py") or something like that?
    GRAPH               = (1, "Graph")
    UNIT_CONV              = (2, "Unit Converter")
    # ALGEBRA             = (4, "") #solve algebraic equations and trigonometric identities
    # CALCULUS            = (5, "") #differentiation and integration
    # TIP_CALC            = (6, "")
    # EXPORT              = (7, "")
        
class KeyboardDisplayMode(BaseEnum):
    BASIC                   = (0, "Basic") #do we want to add (1,"evaluator_algebra.py") or something like that?
    FUNCTIONS               = (1, "Functions") #do we want to add (1,"evaluator_algebra.py") or something like that?