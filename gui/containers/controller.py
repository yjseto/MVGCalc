from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from lib.enums.keys import *
from lib.enums.constants import *
from lib.models.result import IResult
from lib.enums.modes import *
from lib.util.evaluator import evaluate

from gui.containers.app import MvgCalcApplication
from gui.components.navigation import NavBar
from gui.components.keyboard import *
from gui.components.listbox import HistoricExpressionListWidget

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Keyboard

Container component for keyboard button navigation component,
basic keyboard, and functions keyboard.

This keyboard component acts as the controller for user keyboard input.
All signals from child components are recieved and the either a request 
to the evaluator service made or the user_input model is updated.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class KeyInputController(QWidget):

    #after button click return display text including updated inputs
    return_result = pyqtSignal(IResult)
    refresh_expr_screen = pyqtSignal()
    clear_graph = pyqtSignal()

    def __init__(self, app : MvgCalcApplication):
        super().__init__()

        self.app = app
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.stack_layout = QStackedWidget()

        self.key_display = KeyboardDisplayMode.BASIC
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Navbar
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        
        self.navbar = NavBar(
            KeyboardDisplayMode.BASIC,
            KeyboardDisplayMode.FUNCTIONS,
            KeyboardDisplayMode.HISTORIC_EXPRESSIONS
        )
        self.navbar.clicked_display_signal.connect(self.activate_tab)
        self.main_layout.addLayout(self.navbar)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Basic Keyboard
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.basic_keys = BasicKeyboard()
        self.stack_layout.addWidget(self.basic_keys)
        self.basic_keys.button_click_signal_from_keyboard.connect(self.handle_button_click)
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Function Keyboard
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.func_keys = FunctionKeyboard()
        self.stack_layout.addWidget(self.func_keys)
        self.func_keys.button_click_signal_from_keyboard.connect(self.handle_button_click)

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Historic Expression Listbox
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.hist_expr_listbox = HistoricExpressionListWidget()
        self.stack_layout.addWidget(self.hist_expr_listbox)
        #self.hist_expr_listbox.button_click_signal_from_keyboard.connect(self.handle_button_click)        

        self.main_layout.addWidget(self.stack_layout)

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # click handler functions
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def handle_button_click(self, key_type : BaseEnum):
        #result: IResult
        if key_type == ActionKey.CLEAR:
            self.app.user_input.clear_list()
            self.refresh_expr_screen.emit()
            self.clear_graph.emit()
        elif key_type == ActionKey.BACKSPACE:
            if not self.app.user_input.is_empty():
                self.app.user_input.pop_from_list()
                self.refresh_expr_screen.emit()
        elif key_type == ActionKey.ENTER:
            result = evaluate(self.app.display_mode, self.app.user_input) 
            self.return_result.emit(result)
        elif isinstance(key_type, ActionKey):
            pass
        elif isinstance(key_type, EvalEnum):    
            self.app.user_input.add_to_list(key_type)
            self.refresh_expr_screen.emit()

    def activate_tab(self, display_type : KeyboardDisplayMode):
        self.key_display = display_type
        self.stack_layout.setCurrentIndex(display_type.index)