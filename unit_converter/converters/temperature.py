from conveter_base import ConverterBase
from unit_converter.models.user_input import UserInput
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class ConverterTemperature():

    def __init__(self):
        #i think the best way to do this is to have a base unit, then build off of that
        #using a dictionary
        self.unit_table = {'fahrenheit' : 1, 'celcius': -17.222222222, 'kelvin': 255.92777778}
        

        #work in progress
    
    def convert(self,value, unit1,unit2):
        #you'd have a list inputted like [1,'mile',0,'kilometer']
        result = value
        #will have to be custom for temp
        return result
            
convert_test = ConverterTemperature()

print(convert_test.convert(32,'fahrenheit','celcius'))
