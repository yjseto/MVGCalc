# Easy path, We can use this if we want to just pass everything to eval(string), warning security concerns with eval()
# because it will execute python code.
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, transformations

def evaluate(expression):
    #takes a string as an input
    #puts it into sympy readable language
    #evaluates it if arithmatic, symplifies if uses symbols
    #result will be able to be used with more advanced math like calculus 
    parsed_expr = parse_expr(expression,transformations='all')
    result = sp.sympify(parsed_expr).evalf()
    return result

#utility class - user input validation (maybe create a new class for validation), formatting, etc...


