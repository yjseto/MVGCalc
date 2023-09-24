from PyQt5.QtWidgets import *

class PyQtModel:
    main_menu_items = [
        "Calculator Display",
        "Calculus Display",
        "Graph Display",
        "Graph Coordinate Display",
        "Probability Display",
        "Tip Calculator Display",
        "Unit Conversion Display"
    ]

# binds the model and the view
class PyQtController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)

        self.list_widget.itemDoubleClicked.connect(self.item_double_clicked)

    def item_double_clicked(self, item):
        # Handle the item double-click event
        print(f"Item Double-Clicked: {item.text()}")

class PyQtView(QMainWindow):
    def __init__(self, parent=None):
        super(PyQtView, self).__init__(parent)  

    def setup(self):

        self.setWindowTitle('ListWidget Example')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a QListWidget
        self.list_widget = QListWidget()

        # Add items to the list
        items = PyQtModel.main_menu_items
        for item_text in items:
            item = QListWidgetItem(item_text)
            self.list_widget.addItem(item)

        layout.addWidget(self.list_widget)
        central_widget.setLayout(layout)


# class MainMenuWindow:
#     def __init__(self): 
#         PyQtController(PyQtModel, PyQtView).start()
        

# class UIFunctionList(QWidget):
#     def __init__(self, parent=None):
#         super(UIFunctionList, self).__init__(parent)
#         # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
#         self.ToolsBTN = QPushButton('Back', self)
#         self.ToolsBTN.move(10, 10)
        
#         self.Graphing = QPushButton('Plot Graph', self)
#         self.Graphing.move(10, 50)
        
#         self.Math = QPushButton('Math', self)
#         self.Math.move(120, 50)
        
#         self.BASIC_DISP = QPushButton('BASIC_DISP', self)
#         self.BASIC_DISP.move(230, 50)
        
#         self.GRAPH_DISP = QPushButton('GRAPH_DISP', self)
#         self.GRAPH_DISP.move(10, 100)
        
#         self.GRAPH_CHART_DISP = QPushButton('GRAPH_CHART_DISP', self)
#         self.GRAPH_CHART_DISP.move(10, 150)
        
#         self.TRIG_DISP = QPushButton('TRIG_DISP', self)
#         self.TRIG_DISP.move(150, 150)
        
#         self.CALCULUS_DISP = QPushButton('CALCULUS_DISP', self)
#         self.CALCULUS_DISP.move(10, 200)
        
#         self.TIP_CALC_DISP = QPushButton('TIP_CALC_DISP', self)
#         self.TIP_CALC_DISP.move(10, 250)
       
#         self.UNIT_CONVERSION_DISP = QPushButton('UNIT_CONVERSION_DISP', self)
#         self.UNIT_CONVERSION_DISP.move(10, 300)
        
#         self.PROBABILITY_DISP = QPushButton('PROBABILITY_DISP', self)
#         self.PROBABILITY_DISP.move(10, 350)



# class UIMenu(QWidget):
#     def __init__(self, parent=None):
#         super(UIMenu, self).__init__(parent)
#         self.CPSBTN = QPushButton("Menu", self)
#         self.CPSBTN.move(300, 10)


# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setGeometry(50, 50, 400, 450)
#         self.setFixedSize(400, 450)
#         self.startUIMenu()

#     def startUIMenu(self):
#         self.ToolTab = UIMenu(self)
#         self.setWindowTitle("Main Menu")
#         self.setCentralWidget(self.ToolTab)
#         self.ToolTab.CPSBTN.clicked.connect(self.startUIFunctionList)
#         self.show()

#     def startUIFunctionList(self):
#         self.Window = UIFunctionList(self)
#         self.setWindowTitle("Functions")
#         self.setCentralWidget(self.Window)
#         self.Window.ToolsBTN.clicked.connect(self.startUIMenu)
#         self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = MainWindow()
#     sys.exit(app.exec_())