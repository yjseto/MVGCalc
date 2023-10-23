from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
from sympy import N

from lib.models.user_input import UserInput
from lib.enums.modes import DisplayMode

def evaluate_basic(user_input : UserInput):
        try:     
            parsed_in = parse_expr(user_input.format_usr_inp_expr_as_str,transformations='all')  
            return sp.sympify(parsed_in).evalf()
        except Exception as e:
            raise e

def evaluate_graph(user_input : UserInput):
        try:
            to_graph = user_input.format_usr_inp_expr_as_str()
            parsed_expr = parse_expr(to_graph,transformations='all')
            result = N(parsed_expr) #evalf
            result_str = str(result)

            if '.' in result_str:
                result_str = result_str.rstrip('0').rstrip('.')
            return result_str
        except Exception as e:
            raise e

def context(display_mode: DisplayMode, user_input : UserInput):

    if display_mode == DisplayMode.BASIC: 
        return evaluate_basic(user_input)
    
    elif display_mode == DisplayMode.GRAPH: 
        return evaluate_graph(user_input)