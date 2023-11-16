from lib.util.constants import HISTORIC_EXPRESSION_ICON_FILE_PATH

from lib.enums.base import BaseEnum, IconEnum

""" 
    added third property to Display mode enum to include file name for the pkl
    data storage file. this will allow saving expression history specific to the
    display that the expression was evaluated in.
"""
class DisplayMode(BaseEnum):

    BASIC               = (0, "Calculator", "historic_entries_basic.pkl") #do we want to add (1,"evaluator_algebra.py") or something like that?
    GRAPH               = (1, "Graph", "historic_entries_graph.pkl")
    UNIT_CONV           = (2, "Unit Converter", "historic_entries_unit_conv.pkl")
    # ALGEBRA             = (4, "") #solve algebraic equations and trigonometric identities
    # CALCULUS            = (5, "") #differentiation and integration
    # TIP_CALC            = (6, "")
    # EXPORT              = (7, "")

    def __init__ (self, index, textId, data_store_file_name):
        super().__init__(index, textId)  

        self.data_store_file_name = data_store_file_name


class KeyboardDisplayMode(IconEnum):
    BASIC                   = (0, "Basic", None) #do we want to add (1,"evaluator_algebra.py") or something like that?
    FUNCTIONS               = (1, "Functions", None) #do we want to add (1,"evaluator_algebra.py") or something like that?
    HISTORIC_EXPRESSIONS    = (2, "History", HISTORIC_EXPRESSION_ICON_FILE_PATH)