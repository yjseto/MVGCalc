from PyQt5.QtWidgets import QPushButton

class MvgCalcKeyButton(QPushButton):
    def __init__(self, text, _value, _list : list, _dim, parent=None):
        super().__init__(text, parent)

        self.list = _list
        self.value = _value
        self.setGeometry(_dim)
        
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #0060E5;
                color: #CBE1FF;
                border-radius: 2px;
                border-top-right-radius: 8px;
                font-family: roboto;
                font-size: 38px;
            }
            """
        )      

    def mousePressEvent(self, event):
        self.list.append(self.value)
        print(self.list)