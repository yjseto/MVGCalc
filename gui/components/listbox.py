from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from lib.enums.modes import DisplayMode
from lib.util.persistence import MvgCalcDataBuffer
from lib.models.user_input import UserInput

class HistoricExpressionListWidget(QListWidget):
    def __init__(self, display_mode : DisplayMode, parent=None):
        super().__init__(parent)

        #listbox config
        self.setAlternatingRowColors(False)  #True to Alternate row colors

        #listbox data
        self.populate_historic_expr_listbox(display_mode)

    def add_expression_to_list(self, text):

        item = QListWidgetItem(text)
        self.addItem(item)

        # Customize the item properties here if needed

    def populate_historic_expr_listbox(self, display_mode : DisplayMode):

        #remove default list item to No History or previous list
        self.clear()

        self.mvg_calc_buffer = MvgCalcDataBuffer(display_mode)

        #set default list item to No History
        self.insertItem(0,"No history")
        historic_expr_list = self.mvg_calc_buffer.load_all()

        if len(historic_expr_list) > 0:
            self.populate_historic_expr_listbox_from_disk(historic_expr_list)

    def populate_historic_expr_listbox_from_disk(self, historic_expr_list : list[UserInput]):

        #remove default list item to No History or previous list
        self.clear()

        for i, expression in enumerate(historic_expr_list):

            assert isinstance(i, int)
            assert isinstance(expression, UserInput)

            self.insertItem(i, expression.format_usr_inp_expr_as_str(True))
