import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QApplication

#button
class GrandchildWidget(QWidget):
    grandchildSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Grandchild Button")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.handle_grandchild_button_click)

    def handle_grandchild_button_click(self):
        self.grandchildSignal.emit("Signal from Grandchild")

#keyboard
class ChildWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.grandchild = GrandchildWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.grandchild)
        self.setLayout(self.layout)

#display
class ParentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.child = ChildWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.child)
        self.setLayout(self.layout)

        # Connect the grandchild's signal to a slot in the parent
        self.child.grandchild.grandchildSignal.connect(self.handle_grandchild_signal)

    def handle_grandchild_signal(self, message):
        print("Parent received:", message)

def main():
    try:
        app = QApplication(sys.argv)
        parent = ParentWidget()
        parent.show()
        app.exec_()
    except Exception as e:
        # Handle the exception gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
