from libs.evaluator_base import EvaluatorBase
import sympy as sp
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class EvaluatorCalculus(EvaluatorBase):

    def evaluate(expression,operation,variable): 
        parsed_in = parse_expr(expression,transformations='all')
        if operation == 1: #differentiation
            return diff(sp.sympify(parsed_in),variable) #degree of differentation possibly too
        #operation 2 integration?
