from conveter_base import ConverterBase
from unit_converter.models.user_input import UserInput
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class ConverterLength():

    def __init__(self):
        #i think the best way to do this is to have a base unit, then build off of that
        #using a dictionary
        self.unit_table = {'meter': 1, 'kilometer' : 1000, 
                           'centimeter' : 0.01, 'milimeter' : 0.001,
                           'micrometer' : 0.000001, 'nanometer' : 0.0000000001,
                           'mile' : 1609.35, 'yard' : 0.9144, 'foot' : 0.3048,
                           'inch' : 0.0254}
        

        #work in progress
    
    def convert(self,value, unit1,unit2):
        #you'd have a list inputted like [1,'mile',0,'kilometer']
        result = value * self.unit_table[unit1] / self.unit_table[unit2]
        return result
            
convert_test = ConverterLength()

print(convert_test.convert(1,'mile','kilometer'))
