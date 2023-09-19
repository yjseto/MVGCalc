from abc import ABC, abstractmethod

class IEvaluator(ABC):

    # Evaluate list items in userEntries list
    # Parameters:
    #   userEntries: list. a heterogeneous list of numeric values and enumerations representing user input
    # Returns: 
    #   Float | Integer | String?
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def cleanUp(self):
        #if userEntries list is passed by reference we can clear the list here in this abstract class
        pass