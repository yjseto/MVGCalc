from PyQt5.QtWidgets import QListWidget, QListWidgetItem


class HistoricExpressionListWidget(QListWidget):
    def __init__(self):
        super().__init__()

        # Customize the appearance and behavior here
        self.setAlternatingRowColors(True)  # Example: Alternate row colors

    def add_item(self, text):
        item = QListWidgetItem(text)
        self.addItem(item)
        # Customize the item properties here if needed

    # Add more custom methods or override methods as required
