from enum import Enum

class Modes(Enum):
    ARITHMATIC          = 1 #do we want to add (1,"evaluator_algebra.py") or something like that?
    GRAPHING            = 2
    ALGEBRA             = 3 #solve algebraic equations and trigonometric identities
    CALCULUS            = 4 #differentiation and integration
    TIP_CALC            = 5
    EXPORT              = 6

    def retrieve(self):
        return self.value[1]