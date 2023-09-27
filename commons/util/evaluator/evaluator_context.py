from .evaluator_arithmatic import EvaluatorArithmatic
from .evaluator_calculus import EvaluatorCalculus

class EvaluatorContext():
    
    def __init__(self,mode):
        self.mode = mode

    def getEvaluator(self):
        if self.mode == 1:
            return EvaluatorArithmatic
        if self.mode == 2:
            return EvaluatorCalculus
        