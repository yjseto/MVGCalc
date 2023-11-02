import math
from commons.models.user_input import UserInput

def evaluate(expr):
    try:
        x = eval(expr)
        return x
    except:
        print("An exception occured")


if __name__ == '__main__':
    expr = ""
    #input("Enter a math equation: ")
    user_input = UserInput([1,"Operator.ADD",2],1,"")
    print(user_input.format_usr_inp_expr_as_str())

    #can evaluate with letters like x if it is defined as some number
    #eval can take global and local parameters
    #security issues
    # ^ operator is XOR not power
    #can evaluate linear equations by transforming them into a complex equation
    #https://www.geeksforgeeks.org/solve-linear-equations-using-eval-in-python/ 
    #i definetly think its possible to write our own code for arithmatic
    #but if we want to do calculus its better to use a library
    #but if we want to do calculus its better to use a library
