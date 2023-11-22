from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from lib.enums.converter_enums import Length

class legnthListbox(QListWidget):
    switch_window_1 = pyqtSignal()
    switch_window_2 = pyqtSignal()

    unit_1 = pyqtSignal(Length)
    unit_2 = pyqtSignal(Length)

    def __init__(self):
        super().__init__()

        self.target = 0
        # Customize the appearance and behavior here
        #will change these items to baseEnum and have a dictionary to map what was clicked
        #self.setAlternatingRowColors(True)  # Example: Alternate row colors
        self.add_item(Length.METER.textSymbol)
        self.add_item(Length.KILOMETER.textSymbol)
        self.add_item(Length.CENTIMETER.textSymbol)
        self.add_item(Length.MILIMETER.textSymbol)
        self.add_item(Length.MICROMETER.textSymbol)
        self.add_item(Length.NANOMETER.textSymbol)
        self.add_item(Length.MILE.textSymbol)
        self.add_item(Length.YARD.textSymbol)
        self.add_item(Length.FOOT.textSymbol)
        self.add_item(Length.INCH.textSymbol)
       
        #dictionary to match string key to enumeration to find ratio for convert function
        self.length_enum = {
            Length.METER.textSymbol: Length.METER,
            Length.KILOMETER.textSymbol: Length.KILOMETER,
            Length.CENTIMETER.textSymbol: Length.CENTIMETER,
            Length.MILIMETER.textSymbol: Length.MILIMETER,
            Length.MICROMETER.textSymbol: Length.MICROMETER,
            Length.NANOMETER.textSymbol: Length.NANOMETER,
            Length.MILE.textSymbol: Length.MILE,
            Length.YARD.textSymbol: Length.YARD,
            Length.FOOT.textSymbol: Length.FOOT,
            Length.INCH.textSymbol: Length.INCH
        }

        self.itemClicked.connect(self.item_clicked)


    def add_item(self, text):
        item = QListWidgetItem(text)
        self.addItem(item)
        # Customize the item properties here if needed

    def item_clicked(self):
        item = self.currentItem()
        l_type = item.text()
        if self.target == 1:
            self.unit_1.emit(self.length_enum[l_type])
            self.switch_window_1.emit()
        else:
            self.unit_2.emit(self.length_enum[l_type])
            self.switch_window_2.emit()
        
    # Add more custom methods or override methods as required
