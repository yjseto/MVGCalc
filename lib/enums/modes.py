from lib.util.constants import HISTORIC_EXPRESSION_ICON_FILE_PATH

from lib.enums.base import IconEnum

class DisplayMode(IconEnum):
    BASIC               = (0, "Calculator", None) #do we want to add (1,"evaluator_algebra.py") or something like that?
    GRAPH               = (1, "Graph", None)
    UNIT_CONV           = (2, "Unit Converter", None)
    # ALGEBRA             = (4, "") #solve algebraic equations and trigonometric identities
    # CALCULUS            = (5, "") #differentiation and integration
    # TIP_CALC            = (6, "")
    # EXPORT              = (7, "")

class KeyboardDisplayMode(IconEnum):
    BASIC                   = (0, "Basic", None) #do we want to add (1,"evaluator_algebra.py") or something like that?
    FUNCTIONS               = (1, "Functions", None) #do we want to add (1,"evaluator_algebra.py") or something like that?
    HISTORIC_EXPRESSIONS    = (2, "History", HISTORIC_EXPRESSION_ICON_FILE_PATH)