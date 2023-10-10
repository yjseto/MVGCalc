
import sys
from PyQt5.QtWidgets import *
from gui.app import MvgCalcApplication
from gui.components.keyboard import BasicKeyboard



def main():
    app = MvgCalcApplication(sys.argv)
    window = CustomMainWindow(app)
    window.show()
    sys.exit(app.exec_())


class CustomMainWindow(QMainWindow):
    def __init__(self, _app):
        super().__init__()
        self.app = _app

        custom_widget = BasicKeyboard(self.app.user_input)

        self.setCentralWidget(custom_widget)

        self.setWindowTitle("Custom MainWindow Example")
        self.setGeometry(400, 400, 400, 400)

if __name__ == "__main__":
    main()


