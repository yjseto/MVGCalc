from enum import Enum

class Operator(Enum):
    ADD      = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE   = 4

class Operation(Enum):
    ADD        = Operator.ADD
    SUBTRACT   = Operator.SUBTRACT
    MULTIPLY   = Operator.MULTIPLY
    DIVIDE     = Operator.DIVIDE

    def perform(self, x : float | int, y : float | int):
        if self == Operation.ADD:
            return x + y
        elif self == Operation.SUBTRACT:
            return x - y
        elif self == Operation.MULTIPLY:
            return x * y
        elif self == Operation.DIVIDE:
            if y == 0:
                raise ValueError("Cannot divide by zero")
            return x / y
        
# operation = Operation.ADD
# result = operation.perform(5, 3)