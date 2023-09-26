from PyQt5.QtWidgets import QApplication
from commons.models.app_state import AppState

class MvgCalcApplication(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.app_state = AppState  # Store your application-wide state
