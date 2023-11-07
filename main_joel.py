import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Text Wrapping in QLabel")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.label = QLabel()
        self.label.setWordWrap(True)  # Set word wrap to True
        layout.addWidget(self.label)

        update_button = QPushButton("Update Label Text", self)
        layout.addWidget(update_button)
        update_button.clicked.connect(self.update_label_text)

    def update_label_text(self):
        new_text = "This is a long text that will be wrapped within the QLabel to fit the width of the QLabel. " * 5
        self.label.setText(f"<html>{new_text}</html>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
