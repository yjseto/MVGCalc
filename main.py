import sys
#from commons.util.evaluator.evaluator_calculus import EvaluatorCalculus
from gui.app import MvgCalcApplication
from gui.displays.basic import BasicCalcDisplay

def main():
    app = MvgCalcApplication(sys.argv)
    window = BasicCalcDisplay(app)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
