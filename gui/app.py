from PyQt5.QtWidgets import QApplication

class MvgCalcApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.user_input = []
