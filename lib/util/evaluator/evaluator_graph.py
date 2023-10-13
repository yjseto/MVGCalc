from sympy.parsing.sympy_parser import parse_expr
import matplotlib as mpl
from matplotlib import rcParams
from .evaluator_base import EvaluatorBase
from lib.models.user_input import UserInput
import sympy as sp
from sympy import *
#sp.plot(sp.sin(x))

class Graph(EvaluatorBase):

    def __init__(self):
        self.expression = ""

    def evaluate(user_input : UserInput):
        parsed_expr = parse_expr(user_input.format_usr_inp_expr_as_str,transformations='all')
        return parsed_expr

    def graph(expression):
        parsed_expr = parse_expr(expression,transformations='all')
        result = sp.sympify(parsed_expr)
        print(result)
        rcParams['figure.figsize'] = (12,9)
        sp.plot(result)
        
