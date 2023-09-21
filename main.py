from libs.evaluator_workflow import evalWorkflow
from libs.evaluator_arithmatic import EvaluateArithmatic

#mode = 1
mode = 2

exprStr = "2+2"
exprStr1 = "3x**2"

evalWorkMode1 = evalWorkflow(1)
evalWorkMode2 = evalWorkflow(2)

result = evalWorkMode1.getEvaluator().evaluate(exprStr)
result1 = evalWorkMode2.getEvaluator().evaluate(exprStr1,1,'x')

print(result)
print(result1)