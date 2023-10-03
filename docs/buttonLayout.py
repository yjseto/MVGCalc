import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Calculator")
    window.setGeometry(100, 100, 400, 400)

    # Create a layout
    layout = QVBoxLayout()
    
    
    #create a grid layout for the buttons on TOP of line text edit
    grid_layout_top = QGridLayout()
    calc_button = QPushButton("Calculator")
    graph_button = QPushButton("Graph")
    menu_button = QPushButton("Menu")
    history_button = QPushButton("History")
    
    grid_layout_top.addWidget(calc_button,0,0)
    grid_layout_top.addWidget(graph_button,0,1)
    grid_layout_top.addWidget(menu_button,0,2)
    grid_layout_top.addWidget(history_button,1,3)
    
    layout.addLayout(grid_layout_top)

    # Create a line text editor widget for the display
    display = QLineEdit()
    display.setAlignment(Qt.AlignCenter)
    layout.addWidget(display)

    # Create a grid layout for the buttons on BOTTOM of line text edit
    grid_layout_bottom = QGridLayout()

    # Button labels
    buttons = [
        'AC', '( )', '%', '/',
        '7', '8', '9', 'x',
        '4', '5', '6', '-',
        '1', '2', '3', '+',
        '+/-', '0', '.', '='
    ]

    # Create and add buttons to the grid layout
    trig_button = QPushButton("Trig")
    grid_layout_bottom.addWidget(trig_button, 0, 0)
    
    adv_button = QPushButton("Adv")
    grid_layout_bottom.addWidget(adv_button, 0,1)
    
    
    row, col = 1, 0
    for button_label in buttons:
        button = QPushButton(button_label)
        grid_layout_bottom.addWidget(button, row, col)
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Add the grid layout to the main layout
    layout.addLayout(grid_layout_bottom)

    # Set the layout for the main window
    window.setLayout(layout)

    # Show the main window
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
