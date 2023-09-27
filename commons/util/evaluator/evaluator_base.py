from abc import ABC, abstractmethod
from commons.models.user_input import UserInput

class EvaluatorBase(ABC):

    # Evaluate list items in userEntries list
    # Parameters:
    #   userEntries: list. a generic list of numeric values and enumerations representing user input
    # Returns: 
    #   Float | Integer | String?
    @abstractmethod
    def evaluate(self, user_input : UserInput):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def cleanUp(self):
        #if userEntries list is passed by reference we can clear the list here in this abstract class
        pass