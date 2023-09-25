from PyQt5.QtWidgets import QMainWindow, QListWidget, QVBoxLayout, QWidget

class MenuListModel:
    def __init__(self):
        self.items = [
        "Calculator Display",
        "Calculus Display",
        "Graph Display",
        "Graph Coordinate Display",
        "Probability Display",
        "Tip Calculator Display",
        "Unit Conversion Display"            
    ]

    def add_item(self, item_text):
        self.items.append(item_text)

    def get_items(self):
        return self.items

class MenuListView(QListWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.update_view()

    def update_view(self):
        self.clear()
        for item in self.model.get_items():
            self.addItem(item)

class MenuListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self, item_text):
        self.model.add_item(item_text)
        self.view.update_view()


class MenuMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.model = MenuListModel()
        self.menu_list = MenuListView(self.model)
        layout.addWidget(self.menu_list)

        self.controller = MenuListController(self.model, self.menu_list)

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