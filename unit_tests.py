import unittest
from commons.models.user_input import UserInput
from commons.enums.keys.operators import Operator
from commons.enums.keys.character_inputs import CharacterInput
from commons.enums.keys.math_functions import MathFunction
import math

class TestEvalOutput(unittest.TestCase):

    def test_in_1(self):
        user_input2 = UserInput([MathFunction.ABSOLUTE_VAL,CharacterInput.LEFT_P,-2,CharacterInput.RIGHT_P],[])
        formatted_in = user_input2.format_usr_inp_expr_as_str()
        result = eval(formatted_in)
        self.assertAlmostEqual(result,2.0)
        #can make tests better by writing several tests
        #test edge cases


#class TestEvalInput(unittest.TestCase): #could use this to test input assertions

    #def test_in_1(self):
        #pass

#rescource
#https://www.youtube.com/watch?v=6tNS--WetLI

if __name__ == "__main__":
    unittest.main()


    