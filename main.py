import sys
#from ui.state.mvgcalc_applicaton import MvgCalcApplication
#from ui.displays.menus.display_main_menu import MenuMenu
from commons.models.user_input import UserInput
from commons.enums.keys.operators import Operator
from commons.enums.keys.character_inputs import CharacterInput
from commons.enums.keys.math_functions import MathFunction

def main():
    #app = MvgCalcApplication(sys.argv)
    #window = MenuMenu()
    #window.show()
    #sys.exit(app.exec_())
    


    #This is how UserInput would take a list
    #test
    user_input = UserInput([2,Operator.EXPONENT,2,Operator.SUBTRACT,CharacterInput.LEFT_P,1,CharacterInput.RIGHT_P],[])
    formatted_in = user_input.format_usr_inp_expr_as_str()
    print(formatted_in)
    print(eval(formatted_in))

if __name__ == "__main__":
    main()
    


# from commons.util.evaluator.evaluator_context import EvaluatorContext

# #mode = 1
# mode = 2

# #exprStr = "2+2"
# exprStr1 = "3x**2"

# #evalWorkMode1 = EvaluatorContext(1)
# evalWorkMode2 = EvaluatorContext(2)

# #result = evalWorkMode1.getEvaluator().evaluate(exprStr)
# result1 = evalWorkMode2.getEvaluator().evaluate(exprStr1,1,'x')

# #print(result)
# print(result1)