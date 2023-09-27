from .evaluator_base import EvaluatorBase
from commons.models.user_input import UserInput
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class EvaluatorArithmatic(EvaluatorBase):

    def evaluate(user_input : UserInput):
        parsed_in = parse_expr(user_input.format_usr_inp_expr_as_str,transformations='all')
        return sp.sympify(parsed_in).evalf()
    
    # I kept this here so your test harness still works remove it when you implement evaluate
    # using UserInput- joel
    def evaluate(expression):
        parsed_in = parse_expr(expression,transformations='all')
        return sp.sympify(parsed_in).evalf()


