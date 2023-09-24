from libs.evaluator_base import EvaluatorBase
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class EvaluatorArithmatic(EvaluatorBase):

    def evaluate(expression):
        parsed_in = parse_expr(expression,transformations='all')
        return sp.sympify(parsed_in).evalf()

