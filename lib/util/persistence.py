import os
import pickle as pk
from pathlib import Path
from typing import List

from lib.enums.modes import DisplayMode
from lib.models.user_input import UserInput
from lib.util.utils import get_project_root

class MvgCalcDataBuffer:

    def __init__(self, display_mode : DisplayMode):

        project_context = get_project_root()

        self.data_store_file_path =  Path(f"{project_context}\data\{display_mode.data_store_file_name}")
        
    def save_expression_to_disk(self, evaluated_expression : UserInput):

        try:

            historic_expressions : List[UserInput] = self.load_all()

            # Add current expression
            historic_expressions.append(evaluated_expression)
            
            # Save the updated historic expressions list back to file
            with open(self.data_store_file_path, 'wb') as rf:
                pk.dump(historic_expressions, rf)
                rf.close()

        except (FileNotFoundError):
            #moro you usually want to handle the exception in a way that allows the program to 
            #halt execution gracefully and display/log an error messages. you were swallowing 
            #the exception which is a code smell. i will handle these exceptions in the next delivery
            #TODO handle exception
            print("throw exception")

    #Returns a list of UserInput objects for further evaluation 
    def load_all(self) -> List[UserInput]: 

        historic_expressions : List[UserInput] = []

        try:

            # if pickle does not exist create a new .pkl file with an empty list
            if not self.data_store_file_path.exists():
                with open(self.data_store_file_path, 'wb') as rf:
                    pk.dump(historic_expressions, rf)
            else:
                # Load the existing historic expressions list from the file
                with open(self.data_store_file_path, 'rb') as rf:
                    historic_expressions = pk.load(rf)

        except (FileNotFoundError):
            #TODO handle exception
            print("throw exception")

        return historic_expressions


    def delete_expression_at_index(self, index : int):

        try:

            historic_expressions : List[UserInput] = self.load_all()

            # Add current expression
            historic_expressions.pop(index)
            
            # Save the updated historic expressions list back to file
            with open(self.data_store_file_path, 'wb') as rf:
                pk.dump(historic_expressions, rf)
                rf.close()

        except (FileNotFoundError):
            #moro you usually want to handle the exception in a way that allows the program to 
            #halt execution gracefully and display/log an error messages. you were swallowing 
            #the exception which is a code smell. i will handle these exceptions in the next delivery
            #TODO handle exception
            print("throw exception")        

    def delete_history_by_display(self):
        try:
            if os.path.exists(self.data_store_file_path):
                os.remove(self.data_store_file_path)
        except OSError as e:
            #TODO handle exception
            print("throw exception")     





