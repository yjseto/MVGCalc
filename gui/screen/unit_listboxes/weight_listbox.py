from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from lib.enums.converter_enums import Weight

class weightListbox(QListWidget):
    switch_window_1 = pyqtSignal()
    switch_window_2 = pyqtSignal()

    unit_1 = pyqtSignal(Weight)
    unit_2 = pyqtSignal(Weight)

    def __init__(self):
        super().__init__()
        self.target = 0
        # Customize the appearance and behavior here
        #will change these items to baseEnum and have a dictionary to map what was clicked
        #self.setAlternatingRowColors(True)  # Example: Alternate row colors
        self.add_item(Weight.KILOGRAM.textSymbol)
        self.add_item(Weight.GRAM.textSymbol)
        self.add_item(Weight.MILIGRAM.textSymbol)
        self.add_item(Weight.METRIC_TON.textSymbol)
        self.add_item(Weight.POUND.textSymbol)
        self.add_item(Weight.OUNCE.textSymbol)
        self.add_item(Weight.CARAT.textSymbol)
        
        self.weight_enum = {
            Weight.KILOGRAM.textSymbol: Weight.KILOGRAM,
            Weight.GRAM.textSymbol: Weight.GRAM,
            Weight.MILIGRAM.textSymbol: Weight.MILIGRAM,
            Weight.METRIC_TON.textSymbol: Weight.METRIC_TON,
            Weight.POUND.textSymbol: Weight.POUND,
            Weight.OUNCE.textSymbol: Weight.OUNCE,
            Weight.CARAT.textSymbol: Weight.CARAT
        }
        
        self.itemClicked.connect(self.item_clicked)


    def add_item(self, text):
        item = QListWidgetItem(text)
        self.addItem(item)
        # Customize the item properties here if needed

    def item_clicked(self):
        item = self.currentItem()
        w_type = item.text()
        if self.target == 1:
            self.unit_1.emit(self.weight_enum[w_type])
            self.switch_window_1.emit()
        else:
            self.unit_2.emit(self.weight_enum[w_type])
            self.switch_window_2.emit()
    # Add more custom methods or override methods as required
