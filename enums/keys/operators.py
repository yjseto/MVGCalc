from enum import Enum

class Operator(Enum):
    ADD      = (1,"+")
    SUBTRACT = (2,"-")
    MULTIPLY = (3,"*")
    DIVIDE   = (4,"/")
    #(^ on the calc) ** is eval() readable
    EXPONENT = (5,"^ or **")
    

        
        #Think we're going to change this function
        
# operation = Operation.ADD
# result = operation.perform(5, 3)