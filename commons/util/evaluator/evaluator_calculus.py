from .evaluator_base import EvaluatorBase
from commons.models.user_input import UserInput
import sympy as sp
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class EvaluatorCalculus(EvaluatorBase):

    #should be a way to access operation or variable from either the UserInput model or from AppState model
    #i will put it in UserInput model for now
    def evaluate(user_input : UserInput): 
        parsed_in = parse_expr(user_input.format_usr_inp_expr_as_str  ,transformations='all')
        if user_input.operation == 1: #differentiation
            return diff(sp.sympify(parsed_in),user_input.variable) #degree of differentation possibly too
        #operation 2 integration?

    # I kept this here so your test harness still works remove it when you implement evaluate
    # using UserInput- joel
    def evaluate(expression,operation,variable): 
        parsed_in = parse_expr(expression,transformations='all')
        if operation == 1: #differentiation
            return diff(sp.sympify(parsed_in),variable) #degree of differentation possibly too
        #operation 2 integration?
