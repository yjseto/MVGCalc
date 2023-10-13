from .conveter_base import ConverterBase
from unit_converter.models.user_input import UserInput
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

class ConverterLength(ConverterBase):

    def __init__(self):
        #i think the best way to do this is to have a base unit, then build off of that
        self.meter = 1
        self.kilometer = 1000*self.meter
        self.centimeter = 0.01*self.meter
        self.milimeter = 0.001*self.meter
        self.micrometer = 0.000001*self.meter
        self.nanometer = 0.0000000001*self.meter
        self.mile = 1609.35*self.meter
        self.yard = 0.9144*self.meter
        self.foot = 0.3048*self.meter
        self.inch = 0.0254
        

        #work in progress
    
    def convert(user_input):
        #you'd have a list inputted like [1,'mile',0,'kilometer']
        value_to_conv = user_input[0]
        unit_base = user_input[1]
        output_val = user_input[2]
        output_val_unit = user_input[3]
        
        #1 mile would be defined as 1609.35*1 meters
        in_meters = value_to_conv
            

