import sys
from commons.util.evaluator.evaluator_calculus import EvaluatorCalculus
#from ui.state.mvgcalc_applicaton import MvgCalcApplication
#from ui.displays.menus.display_main_menu import MenuMenu

def main():
    #app = MvgCalcApplication(sys.argv)
    #window = MenuMenu()
    #window.show()
    #sys.exit(app.exec_())
    
    #hgow to call the definite integral evaluator
    print(EvaluatorCalculus.integrate_definite("2^x",('x',1,2)))

    print("Hello World")
    #This is how UserInput would take a list
    #test


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