from abc import ABC, abstractmethod
from lib.models.user_input import UserInput

class EvaluatorBase(ABC):

    # Evaluate list items in userEntries list
    # Parameters:
    #   userEntries: list. a generic list of numeric values and enumerations representing user input
    # Returns: 
    #   Float | Integer | String?
    @abstractmethod
    def evaluate(self, user_input : UserInput):
        pass
    
    def clean_up(self, user_input : UserInput):
            user_input.clear_list
        