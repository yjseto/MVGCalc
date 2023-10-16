from .length import ConverterLength
from .weight import ConverterWeight
from .temperature import ConverterTemperature
from .speed import ConverterSpeed


class ConverterContext():
    
    def __init__(self,mode):
        self.mode = mode

    def getEvaluator(self):
        if self.mode == 1:
            return ConverterTemperature
        if self.mode == 2:
            return ConverterSpeed
        if self.mode == 3:
            return ConverterLength
        #if self.mode == 4:
           #return ConverterArea
        if self.mode == 5:
            return ConverterWeight
        