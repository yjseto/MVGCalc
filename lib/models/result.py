from abc import ABC

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

class BasicResult(ResultBase):
    def __init__(self):
        super().__init__()

class GraphResult(ResultBase):
    def __init__(self):
        super().__init__()
        self.y: str
        self.trig_func = False