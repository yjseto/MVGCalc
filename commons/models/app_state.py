from dataclasses import dataclass
from .user_input import UserInput

@dataclass
class AppState:
    """Class for keeping track of an item in inventory."""
    user_input: UserInput
    number_in_progress : str
    mode: int