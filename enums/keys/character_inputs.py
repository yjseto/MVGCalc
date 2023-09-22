from enum import Enum

class CharacterInput(Enum):
    XVAR                = (1,"x")
    DECIMAL             = (2,".")
    LEFTPARENTHESIS     = (3,"(")
    RIGHTPARENTHESIS    = (4,")")
    NEGATIVE            = (5,"-")