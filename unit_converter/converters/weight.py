from conveter_base import ConverterBase
from unit_converter.models.user_input import UserInput
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class ConverterWeight():

    def __init__(self):
        #i think the best way to do this is to have a base unit, then build off of that
        #using a dictionary
        self.unit_table = {'kilogram' : 1, 'gram' : 1000, 'miligram': 1000000,
                           'metric ton': 0.001, 'long ton': 0.0009842,
                           'short ton' : 0.0011, 'pound' : 2.2046,
                           'ounce' : 35.2739, 'carat' : 5000}
        

        #work in progress
    
    def convert(self,value, unit1,unit2):
        #you'd have a list inputted like [1,'mile',0,'kilometer']
        result = value * self.unit_table[unit2] / self.unit_table[unit1]
        return result
            
convert_test = ConverterWeight()

print(convert_test.convert(1,'pound','ounce'))
