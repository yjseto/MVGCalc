from lib.models.user_input import UserInput
from lib.enums.keys import *
from utils.Util import evaluate,evaluate_to_str
import unittest
import math

"""
    IMPORTANT:
        To run this unit test module in a sub directory you must first initialize the environment variable 
        PYTHONPATH (system or user variable) setting the value of the variable to the path to the
        root of the project.

        Ex. /path/to/your/directory/mvgcalc
        
        Also
        Deactivate Virtual Environment, Close VSCode, Open VSCode, Activate Virtual Environment
"""

class TestEvalOutput(unittest.TestCase):

    def test_in_1(self):
        user_input2 = UserInput([MathFunction.ABSOLUTE_VAL,CharacterInput.LEFT_P,-2,CharacterInput.RIGHT_P])
        formatted_in = user_input2.format_usr_inp_expr_as_str()
        result = eval(formatted_in)
        self.assertAlmostEqual(result,2.0)
        #can make tests better by writing several tests
        #test edge cases

    def test_in_2(self):
        user_input2 = UserInput([2,Operator.ADD,10,Operator.MULTIPLY,MathFunction.CUBERT,CharacterInput.LEFT_P,81,CharacterInput.RIGHT_P])
        formatted_in = user_input2.format_usr_inp_expr_as_str()
        result = eval(formatted_in)
        self.assertAlmostEqual(result,45.26748711)
        #can make tests better by writing several tests
        #test edge cases


    def test_in_sympy_1(self): #uses sympy evalutation 
        user_input = UserInput([2,CharacterInput.XVAR,Operator.SUBTRACT,10,MathFunction.SQUARED]) #can add more parameters to test the input
        formatted_in = user_input.format_usr_inp_expr_as_str()
        result = evaluate_to_str(formatted_in) 
        self.assertEqual(result,"2.0*x - 100") #TODO: ask moro about removed decimal
        #can make tests better by writing several tests
        #test edge cases

    def test_in_sympy_2(self):
        user_input = UserInput([TRIGONOMETRY_FUNCTION.SIN,CharacterInput.LEFT_P,CharacterInput.XVAR,CharacterInput.RIGHT_P,Operator.ADD,TRIGONOMETRY_FUNCTION.COS,CharacterInput.LEFT_P,CharacterInput.XVAR,CharacterInput.RIGHT_P])
        formatted_in = user_input.format_usr_inp_expr_as_str()
        result = evaluate_to_str(formatted_in) 
        self.assertEqual(result,"sin(x) + cos(x)")

    def test_in_4(self):
        user_input = UserInput([1,Operator.DIVIDE,0])
        formatted_in = user_input.format_usr_inp_expr_as_str()
        with self.assertRaises(Exception):
            eval(formatted_in)       


    def test_in_5(self):
        user_input = UserInput([MathFunction.LOG,CharacterInput.LEFT_P,0,CharacterInput.RIGHT_P])
        formatted_in = user_input.format_usr_inp_expr_as_str()
        result = eval(formatted_in)
        self.assertEqual(result,0)

    def test_in_5(self):
        user_input = UserInput([MathFunction.LOG,CharacterInput.LEFT_P,10,CharacterInput.RIGHT_P])
        formatted_in = user_input.format_usr_inp_expr_as_str()
        result = eval(formatted_in)
        self.assertEqual(result,2.302585092994046)
#class TestEvalInput(unittest.TestCase): #could use this to test input assertions

    #def test_in_1(self):
        #pass

#rescource
#https://www.youtube.com/watch?v=6tNS--WetLI

if __name__ == "__main__":
    unittest.main()


    