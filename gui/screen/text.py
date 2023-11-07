from PyQt5.QtWidgets import QLabel

class MvgCalcExpression(QLabel):
    def __init__(self):
        super().__init__()

        # Customize the appearance and behavior of the CustomLabel here
        self.setText("This is a custom label")
        self.setStyleSheet("background-color: lightblue; font-size: 18px; padding: 10px;")

        self.setAlignment(Qt.AlignCenter)  # Center-align the text

    def custom_function(self):
        self.setText("Custom function called")