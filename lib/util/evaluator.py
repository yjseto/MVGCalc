import sympy as sp
from sympy import Eq, zoo
from sympy.parsing.sympy_parser import parse_expr

from lib.models.result import BasicResult, GraphResult, IResult
from lib.models.user_input import UserInput
from lib.enums.modes import DisplayMode
from lib.util.persistence import MvgCalcDataBuffer

def evaluate_basic(user_input : UserInput) -> IResult: 

    result  = BasicResult()
    result.expression = user_input.format_usr_inp_expr_as_str(True)
        
    try:     
        parsed_in = parse_expr(user_input.format_usr_inp_expr_as_str(),transformations='all')  
        #return sp.sympify(parsed_in).evalf()
        
        #check if result expression is undefined
        if Eq(parsed_in, zoo):
            result.error_msgs.append(f"{result.expression} is undefined")
        else:                
            result.value = str(sp.sympify(parsed_in).evalf())
            
            #get rid of trailing 0's
            if '.' in result.value:
                result.value = result.value.rstrip('0').rstrip('.')

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
    
    result.success = len(result.error_msgs) == 0
    #don't clear list yet, we want to save whatever enum list held the expression
    return result

def evaluate_graph(user_input : UserInput):
        
        result  = GraphResult()
        result.expression = user_input.format_usr_inp_expr_as_str(True)
        #set x and y vals
        try:     
            formatted_user_input = parse_expr(user_input.format_usr_inp_expr_as_str(),transformations='all')  
            #return sp.sympify(parsed_in).evalf()
            result.y = str(sp.sympify(formatted_user_input).evalf())
            
            #get rid of trailing 0's
            #if '.' in result.value:
                #result.value = result.value.rstrip('0').rstrip('.')

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
        
        result.success = len(result.error_msgs) == 0
        return result

def evaluate(display_mode: DisplayMode, user_input : UserInput) -> IResult:

    result : IResult = None
    mvg_calc_buffer = MvgCalcDataBuffer(display_mode)

    #need to change this function to originally save enums first?
    if display_mode == DisplayMode.BASIC: 
        result = evaluate_basic(user_input)
    elif display_mode == DisplayMode.GRAPH: 
        result = evaluate_graph(user_input)
    
    if result is None:
        print("throw exception")
        return

    if result.success == True: #might not need that
        mvg_calc_buffer.save_expression_to_disk(user_input) #saving expression as UserInput Object
    
    return result