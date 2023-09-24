from libs.evaluator_arithmatic import EvaluateArithmatic
from libs.evaluator_calculus import EvaluateCalculus

class EvaluatorContext():
    
    def __init__(self,mode):
        self.mode = mode

    def getEvaluator(self):
        if self.mode == 1:
            return EvaluateArithmatic
        if self.mode == 2:
            return EvaluateCalculus
        