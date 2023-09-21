import math

def evaluate(expr):
    try:
        x = eval(expr)
        return x
    except:
        print("An exception occured")


if __name__ == '__main__':
    expr = ""
    #input("Enter a math equation: ")
    result = evaluate(expr)

    print(f"Result: {result}")

    #can evaluate with letters like x if it is defined as some number
    #eval can take global and local parameters
    #security issues
    # ^ operator is XOR not power
    #can evaluate linear equations by transforming them into a complex equation
    #https://www.geeksforgeeks.org/solve-linear-equations-using-eval-in-python/ 
    #i definetly think its possible to write our own code for arithmatic
    #but if we want to do calculus its better to use a library
