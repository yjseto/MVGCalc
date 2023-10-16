from abc import ABC, abstractmethod
from unit_converter.models.user_input import UserInput

class ConverterBase(ABC):


    @abstractmethod
    def units(self):
        pass    