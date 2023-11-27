from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtGui import QColor
from gui.enums.styles import COLORS
from lib.enums.keys import ActionKey

from lib.enums.modes import DisplayMode
from lib.util.persistence import MvgCalcDataBuffer
from lib.models.user_input import UserInput

class HistoricExpressionListWidget(QListWidget):
    def __init__(self, display_mode : DisplayMode, parent=None):
        super().__init__(parent)

        self.v_pos : int = None
        self.mvg_calc_buffer : MvgCalcDataBuffer = None
        self.display_mode = display_mode

        #listbox config
        self.setAlternatingRowColors(False)  #True to Alternate row colors
        self.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.setStyleSheet(f"""
                QListWidget::item:selected {{ 
                    background: \"{COLORS.LIGHT_GREY.value}\"; 
                    color: \"{COLORS.WHITE.value}\"; 
                }}""")

        #listbox data
        self.populate_historic_expr_listbox(self.display_mode)

    def create_list_item(self, expression_as_text : str) -> QListWidgetItem:

        item = QListWidgetItem(expression_as_text)

        return item


    def populate_historic_expr_listbox(self, display_mode : DisplayMode):

        #remove default list item to No History or previous list
        self.clear()

        self.mvg_calc_buffer = MvgCalcDataBuffer(display_mode)

        #set default list item to No History
        self.insertItem(0,"No history")

        historic_expr_list = self.mvg_calc_buffer.load_all()

        if len(historic_expr_list) > 0:
            self.populate_historic_expr_listbox_from_disk(historic_expr_list)
            self.item(0).setSelected(True) 
            self.v_pos = 0
            
    def populate_historic_expr_listbox_from_disk(self, historic_expr_list : list[UserInput]):

        #remove default list item to No History or previous list
        self.clear()

        for i, expression in enumerate(historic_expr_list):

            assert isinstance(i, int)
            assert isinstance(expression, UserInput)

            self.insertItem(i, self.create_list_item(expression.format_usr_inp_expr_as_str(True)))
    
    def update(self, action : ActionKey) -> UserInput:

        current_pos = 0

        if action == ActionKey.UP or action == ActionKey.DOWN:
            current_pos = self.set_current_pos(action)

        self.select_item_by_pos(current_pos)

        return self.mvg_calc_buffer.load_all()[current_pos]

    def select_item_by_pos(self, item_index : int):

        selected_item = self.item(item_index)
        selected_item.setSelected(True)


    def set_current_pos(self, action : ActionKey) -> int:

        if self.v_pos is None: 
            self.v_pos = 0
        
        if ActionKey.UP == action:
            if self.v_pos > 0:
                self.v_pos = self.v_pos - 1 
            if self.v_pos >= (self.count() - 1):  
                self.v_pos = self.v_pos - 1
            return self.v_pos
        elif ActionKey.DOWN == action: 
            if self.v_pos < (self.count() - 1):
                self.v_pos = self.v_pos + 1 
            return self.v_pos

    def delete_all(self):

        self.mvg_calc_buffer.delete_history_by_display()
        self.populate_historic_expr_listbox(self.display_mode)
    
    def delete_selected(self):

        if self.v_pos is not None:
            self.takeItem(self.v_pos)
            self.mvg_calc_buffer.delete_expression_at_index(self.v_pos)
            self.v_pos = self.v_pos - 1
            self.populate_historic_expr_listbox(self.display_mode)


    def reset_pos(self):
        self.v_pos = None
