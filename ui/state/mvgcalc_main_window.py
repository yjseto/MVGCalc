from PyQt5.QtWidgets import QApplication, QMainWindow
from commons.models.app_state import AppState

class MvgCalcMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def change_state(self):
        app = QApplication.instance()  # Get the application instance
        if app is not None:
            app_state = AppState
            app_state.mode = 1
            app.app_state = app_state  # Modify the application-wide state
            self.label.setText(f"Application State: {app.app_state.mode}")