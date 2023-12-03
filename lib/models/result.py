from abc import ABC

from lib.enums.base import EvalEnum
from lib.enums.keys import CharacterInput, NumericInput

KEY_INPUT_DICT = {
    "1": NumericInput.ONE,
    "2": NumericInput.TWO,
    "3": NumericInput.THREE,
    "4": NumericInput.FOUR,
    "5": NumericInput.FIVE,
    "6": NumericInput.SIX,
    "7": NumericInput.SEVEN,
    "8": NumericInput.EIGHT,
    "9": NumericInput.NINE,
    "0": NumericInput.ZERO,
    ".": CharacterInput.DECIMAL_POINT,
    "-": CharacterInput.NEGATIVE
}

class ResultBase(ABC):
    def __init__ (self):
        self.value : any = ""
        self.error_msgs : [str] = []
        self.success : bool = False
        self.expression: str = ""

    def get_formatted_error_msg_list(self) -> str:

        error_str = ""

        for error in self.error_msgs:
            error_str = error_str + str(error) + "\n" 

        return error_str
    
    def get_result_as_list(self) -> list[EvalEnum]:
        pass


class BasicResult(ResultBase):
    def __init__(self):
        super().__init__()

    def get_result_as_list(self) -> list[EvalEnum]:

        result_as_list: list[EvalEnum] = []

        for char in enumerate(self.value):
            result_as_list.append(KEY_INPUT_DICT[char[1]])

        return result_as_list


class GraphResult(ResultBase):
    def __init__(self):
        super().__init__()
        self.y: str
        self.trig_func = False

    def get_result_as_list(self) -> list[EvalEnum]:
        return []