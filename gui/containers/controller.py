from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from lib.enums.keys import *
from lib.models.result import ResultBase
from lib.enums.modes import *
from lib.util.evaluator import evaluate

from gui.containers.app import MvgCalcApplication
from gui.components.navigation import NavBar
from gui.components.keyboard import *
from lib.util.persistence import MvgCalcDataBuffer

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
    return_result = pyqtSignal(ResultBase)
    refresh_expr_screen = pyqtSignal(BaseEnum)
    clear_graph = pyqtSignal()

    def __init__(self, app : MvgCalcApplication):
        super().__init__()

        self.app = app
        self.main_layout = QVBoxLayout()

        self.setLayout(self.main_layout)
        self.stack_layout = QStackedWidget()

        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        Navbar
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""        
        self.key_display = KeyboardDisplayMode.BASIC
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
        Historic Expressions
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
        self.hist_expr_display = HistoricExpressionKeyboard(app.display_mode)
        self.stack_layout.addWidget(self.hist_expr_display)
        self.hist_expr_display.button_click_signal_from_keyboard.connect(self.handle_button_click)        

        self.main_layout.addWidget(self.stack_layout)

    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # click handler functions
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def handle_button_click(self, key_type : BaseEnum):
        #result: ResultBase
        if key_type == ActionKey.CLEAR:
            self.app.user_input.clear_list()
            self.app.h_pos = None
            self.refresh_expr_screen.emit(key_type)
            self.clear_graph.emit()
        elif key_type == ActionKey.BACKSPACE:
            if self.key_display == KeyboardDisplayMode.HISTORIC_EXPRESSIONS:
                print("uncomment below then Fix errors when pickle is deleted and directional arrows used")
                #MvgCalcDataBuffer(self.app.display_mode).delete_history_by_display()
            else:
                self.app.user_input.remove_from_list(self.app.h_pos)
                self.refresh_expr_screen.emit(key_type)
        elif key_type == ActionKey.ENTER:
            try:
                if not self.app.user_input.is_empty():
                    self.app.h_pos = None
                    result = evaluate(self.app.display_mode, self.app.user_input) 
                    self.return_result.emit(result)
            except TypeError as e:
                pass
        elif isinstance(key_type, ActionKey):
            self.refresh_expr_screen.emit(key_type)
        # block for all value key inputs
        elif isinstance(key_type, EvalEnum): 
            if DisplayMode.BASIC == self.app.display_mode and key_type == CharacterInput.XVAR:
                return
            
            self.app.user_input.add_to_list(key_type, self.app.h_pos)
            self.refresh_expr_screen.emit(key_type)

    def activate_tab(self, display_type : KeyboardDisplayMode):
        self.key_display = display_type
        if display_type == KeyboardDisplayMode.HISTORIC_EXPRESSIONS:
            self.hist_expr_display.hist_expr_listbox.populate_historic_expr_listbox(self.app.display_mode) #reload with updated expressions
        self.stack_layout.setCurrentIndex(display_type.index)
