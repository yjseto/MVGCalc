from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from lib.enums.converter_enums import Measure

class measuresListbox(QListWidget):
    switch_window = pyqtSignal()
    current_measure = pyqtSignal(Measure)
    def __init__(self):
        super().__init__()

        # Customize the appearance and behavior here
        #self.setAlternatingRowColors(True)  # Example: Alternate row colors
        self.add_item(Measure.LENGTH.textSymbol)
        self.add_item(Measure.WEIGHT.textSymbol)
        self.itemClicked.connect(self.item_clicked)
        self.current_measure_enum = Measure.LENGTH

        self.measure_enum = {
            Measure.LENGTH.textSymbol: Measure.LENGTH,
            Measure.WEIGHT.textSymbol: Measure.WEIGHT
        }

    def add_item(self, text):
        item = QListWidgetItem(text)
        self.addItem(item)
        # Customize the item properties here if needed
    
    def item_clicked(self):
        item = self.currentItem()
        m_type = item.text()

        # Emit the Measure enumeration and switch_window signal
        #self.communication.current_measure.emit()
        self.current_measure.emit(self.measure_enum[m_type])
        self.switch_window.emit()

    # Add more custom methods or override methods as required
