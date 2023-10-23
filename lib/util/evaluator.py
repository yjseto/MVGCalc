from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
from sympy import N
from lib.models.result import BasicResult, IResult
from lib.models.user_input import UserInput
from lib.enums.modes import DisplayMode

def evaluate_basic(user_input : UserInput) -> IResult: 
        result  = BasicResult()
        result.expression = user_input.format_usr_inp_expr_as_str(True)
         
        try:     
            parsed_in = parse_expr(user_input.format_usr_inp_expr_as_str,transformations='all')  
            #return sp.sympify(parsed_in).evalf()
            result.value = sp.sympify(parsed_in).evalf()
            result.success = True

        except ValueError as ve:
            print(f"Value error: {ve}")
            result.error_msgs.append(f"Value error: {ve}")

        except TypeError as te:
            print(f"Tytpe error: {te}")
            result.error_msgs.append(f"Type error: {te}")

        except SyntaxError as se:
            print(f"Syntax error: {se}")
            result.error_msgs.append(f"Syntax error: {se}")

        except NotImplementedError as nie:
            print(f"Not implemented error: {nie}")
            result.error_msgs.append(f"Not implemented error: {nie}")
        except Exception as e:
            raise e

        return result

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

def context(display_mode: DisplayMode, user_input : UserInput) -> IResult:

    if display_mode == DisplayMode.BASIC: 
        return evaluate_basic(user_input)
    
    elif display_mode == DisplayMode.GRAPH: 
        return evaluate_graph(user_input)