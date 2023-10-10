from .evaluator_base import EvaluatorBase
from lib.models.user_input import UserInput
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class EvaluatorArithmatic(EvaluatorBase):

    def evaluate(user_input : UserInput):
        try:
            parsed_in = parse_expr(user_input.format_usr_inp_expr_as_str,transformations='all')
            return sp.sympify(parsed_in).evalf()
        except Exception as e:
            raise e
    



