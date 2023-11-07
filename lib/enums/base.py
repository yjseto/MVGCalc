from enum import Enum

class BaseEnum(Enum):
    def __init__ (self, index, textSymbol):
        self.index = index
        self.textSymbol = textSymbol   

    def get_no_parentheses(self):
        return self.textSymbol.strip('(')

class IconEnum(BaseEnum):
    def __init__ (self, index, textId, iconPath):
        super().__init__(index, textId)
        self.iconPath = iconPath

class EvalEnum(BaseEnum):
    def __init__ (self, index, textId, textEval, textSymbol):
        super().__init__(index, textId)
        self.textEval = textEval
        self.textSymbol = textSymbol
