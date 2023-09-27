from enum import Enum

class CharacterInput(Enum):
    XVAR                = (1,"x")
    DECIMAL             = (2,".")
    LEFT_P              = (3,"(")
    RIGHT_P             = (4,")")
    NEGATIVE            = (5,"-")
    YVAR                = (6,"y")
    ZVAR                = (7,"z")

    def retrieve(self):
        return self.value[1]