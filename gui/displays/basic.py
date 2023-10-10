import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QRect

from gui.components.button import MvgCalcKeyButton
from lib.enums.keys import Operator

# qt_creator_file = "test.ui"
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
# tick = QtGui.QImage('tick.png')

real_list_arr = list()
list_arr = []

#Model
class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        
        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index): #rowcount() method is called by the view to get the number of rows in the current data
        return len(self.todos)






#ViewController
class BasicCalcDisplay(QMainWindow):
    def __init__(self, _app):
        super().__init__()
        self.app = _app

        self.setObjectName("BasicCalcDisplay")
        self.resize(375, 812)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setStyleSheet(
            """
            QWidget {
                background-color: #161A20;
            }
            """
        )    

        self.setupUi()





        #self.mainDisplayTextarea.setModel(self.model)
        #self.threeButton.pressed.connect(self.add)
        #self.btnSubtract.pressed.connect(self.subtract)
        # self.deleteButton.pressed.connect(self.delete)
        # self.completeButton.pressed.connect(self.complete)

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        # Access the list via the model.
        #self.model.todos.append(3)
        self.app.user_input.append(3)
        # Trigger refresh.        
        self.model.layoutChanged.emit()
        # Empty the input
        self.save()

        print(self.app.user_input)

    def subtract(self, app):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        # Access the list via the model.

        app.user_input.append(Operator.SUBTRACT.symbol)
        # Trigger refresh.        
        self.model.layoutChanged.emit()
        # Empty the input
        self.save()    

        print(app.user_input)
    
        
    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a list of a single item in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            #self.save()
            
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal 
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
            self.save()
    
    def load(self):
        try:
            with open('data.db', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)

# Button Press Event 
########################################################################################################## 
# 

    def add_value_to_list(self, value):
        list_arr.append(value)
        print(list_arr)

    def click_zero(self):
        list_arr.append("0")
        print(list_arr)
            
    def click_one(self):
        list_arr.append("1")
        print(list_arr)

    def click_two(self):
        list_arr.append("2")
        print(list_arr)
        
    def click_three(self):
        list_arr.append("3")
        print(list_arr)
        
    def click_four(self):
        list_arr.append("4")
        print(list_arr)
        
    def click_five(self):
        list_arr.append("5")
        print(list_arr)
        
    def click_six(self):
        list_arr.append("6")
        print(list_arr)
        
    def click_seven(self):
        list_arr.append("7")
        print(list_arr)

    def click_eight(self):
        list_arr.append("8")
        print(list_arr)

    def click_nine(self):
        list_arr.append("9")
        print(list_arr)
        
    def click_AC(self):
        list_arr.clear()
        print(list_arr)
        
    def click_plus(self):
        if list_arr != []:
                if (48 <= ord(list_arr[len(list_arr)-1]) <= 57):
                        list_arr.append("+")
        print(list_arr)
            
    def click_minus(self):
        if list_arr != []:
                if (48 <= ord(list_arr[len(list_arr)-1]) <= 57):
                        list_arr.append("-")
        print(list_arr)

    def click_multiplication(self):
        if list_arr != []:
                if (48 <= ord(list_arr[len(list_arr)-1]) <= 57):
                        list_arr.append("*")
        print(list_arr)
        
    def click_division(self):
        if list_arr != []:
                if (48 <= ord(list_arr[len(list_arr)-1]) <= 57):
                        list_arr.append("/")
        print(list_arr)
        
    def click_dot(self):
        if list_arr != []:
                if (48 <= ord(list_arr[len(list_arr)-1]) <= 57):
                        list_arr.append(".")
        print(list_arr)



    def setupUi(self):

        self.keys = QtWidgets.QWidget(self)

        self.division = MvgCalcKeyButton(
             Operator.DIVIDE.textSymbol,        # character displayed on button
             Operator.DIVIDE,                   # value added to array
             self.app.user_input,               # user input array
             QRect(277, 351, 83, 79),           # button dimensions
             self.keys)                                              


        self.multiplication = MvgCalcKeyButton(
             Operator.MULTIPLY.textSymbol,      # character displayed on button
             Operator.MULTIPLY,                 # value added to array
             self.app.user_input,               # user input array
             QRect(277, 351, 83, 79),           # button dimensions
             self.keys)                                        


        self.equal = QtWidgets.QPushButton(self.keys)
        self.equal.setGeometry(QtCore.QRect(277, 683, 83, 79))
        self.equal.setStyleSheet("QPushButton {\n"
"    background-color: #0060E5;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    border-bottom-right-radius: 8px;\n"
"    font-family: roboto;\n"
"font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.equal.setObjectName("equal")


        self.minus = QtWidgets.QPushButton(self.keys)
        self.minus.setGeometry(QtCore.QRect(277, 517, 83, 79))
        self.minus.setStyleSheet("QPushButton {\n"
"    background-color: #0060E5;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.minus.setObjectName("minus")
        self.plus = QtWidgets.QPushButton(self.keys)
        self.plus.setGeometry(QtCore.QRect(277, 600, 83, 79))
        self.plus.setStyleSheet("QPushButton {\n"
"    background-color: #0060E5;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.plus.setObjectName("plus")
        self.AC = QtWidgets.QPushButton(self.keys)
        self.AC.setGeometry(QtCore.QRect(16, 351, 83, 79))
        self.AC.setStyleSheet("QPushButton {\n"
"    background-color: #363E4D;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    border-top-left-radius: 8px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.AC.setProperty("operands", "")
        self.AC.setObjectName("AC")
        self.paranth = QtWidgets.QPushButton(self.keys)
        self.paranth.setGeometry(QtCore.QRect(103, 351, 83, 79))
        self.paranth.setStyleSheet("QPushButton {\n"
"    background-color: #363E4D;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.paranth.setProperty("operands", "")
        self.paranth.setObjectName("paranth")
        self.percent = QtWidgets.QPushButton(self.keys)
        self.percent.setGeometry(QtCore.QRect(190, 351, 83, 79))
        self.percent.setStyleSheet("QPushButton {\n"
"    background-color: #363E4D;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.percent.setProperty("operands", "")
        self.percent.setObjectName("percent")
        self.nine = QtWidgets.QPushButton(self.keys)
        self.nine.setGeometry(QtCore.QRect(190, 434, 83, 79))
        self.nine.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.nine.setProperty("operands", "")
        self.nine.setObjectName("nine")
        self.seven = QtWidgets.QPushButton(self.keys)
        self.seven.setGeometry(QtCore.QRect(16, 434, 83, 79))
        self.seven.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.seven.setProperty("operands", "")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.keys)
        self.eight.setGeometry(QtCore.QRect(103, 434, 83, 79))
        self.eight.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.eight.setProperty("operands", "")
        self.eight.setObjectName("eight")
        self.four = QtWidgets.QPushButton(self.keys)
        self.four.setGeometry(QtCore.QRect(16, 517, 83, 79))
        self.four.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.four.setProperty("operands", "")
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.keys)
        self.five.setGeometry(QtCore.QRect(103, 517, 83, 79))
        self.five.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.five.setProperty("operands", "")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.keys)
        self.six.setGeometry(QtCore.QRect(190, 517, 83, 79))
        self.six.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.six.setProperty("operands", "")
        self.six.setObjectName("six")
        self.one = QtWidgets.QPushButton(self.keys)
        self.one.setGeometry(QtCore.QRect(16, 600, 83, 79))
        self.one.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.one.setProperty("operands", "")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.keys)
        self.two.setGeometry(QtCore.QRect(103, 600, 83, 79))
        self.two.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.two.setProperty("operands", "")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.keys)
        self.three.setGeometry(QtCore.QRect(190, 600, 83, 79))
        self.three.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.three.setProperty("operands", "")
        self.three.setObjectName("three")
        self.dot = QtWidgets.QPushButton(self.keys)
        self.dot.setGeometry(QtCore.QRect(190, 683, 83, 79))
        self.dot.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.dot.setProperty("operands", "")
        self.dot.setObjectName("dot")
        self.zero = QtWidgets.QPushButton(self.keys)
        self.zero.setGeometry(QtCore.QRect(103, 683, 83, 79))
        self.zero.setStyleSheet("QPushButton {\n"
"    background-color: #242933;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.zero.setProperty("operands", "")
        self.zero.setObjectName("zero")
        self.plusNminus = QtWidgets.QPushButton(self.keys)
        self.plusNminus.setGeometry(QtCore.QRect(16, 683, 83, 79))
        self.plusNminus.setStyleSheet("QPushButton {\n"
"    background-color: #363E4D;\n"
"    color: #CBE1FF;\n"
"    border-radius: 2px;\n"
"    border-bottom-left-radius: 8px;\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"   }\n"
"\n"
"")
        self.plusNminus.setProperty("operands", "")
        self.plusNminus.setObjectName("plusNminus")
        self.pushButton = QtWidgets.QPushButton(self.keys)
        self.pushButton.setGeometry(QtCore.QRect(24, 316, 66, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #D9D9D9;\n"
"    color: #212D2A;\n"
"    border-radius: 11px;\n"
"    font-family: roboto;\n"
"    font-size: 17px;\n"
"   }\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.Adv = QtWidgets.QPushButton(self.keys)
        self.Adv.setGeometry(QtCore.QRect(111, 316, 66, 23))
        self.Adv.setStyleSheet("QPushButton {\n"
"    background-color: #D9D9D9;\n"
"    color: #212D2A;\n"
"    border-radius: 11px;\n"
"    font-family: roboto;\n"
"    font-size: 17px;\n"
"   }\n"
"\n"
"")
        self.Adv.setObjectName("Adv")
        self.clock = QtWidgets.QPushButton(self.keys)
        self.clock.setGeometry(QtCore.QRect(252, 129, 95, 25))
        self.clock.setStyleSheet("QPushButton {\n"
"    background-color: #363E4C;\n"
"    color: #CBE1FF;\n"
"    font-weight: lighter;\n"
"    border-radius: 11px;\n"
"    font-family: roboto;\n"
"    font-size: 17px;\n"
"   }\n"
"\n"
"")
        icon = QtGui.QIcon.fromTheme("clock")
        self.clock.setIcon(icon)
        self.clock.setObjectName("clock")
        self.Calc = QtWidgets.QPushButton(self.keys)
        self.Calc.setGeometry(QtCore.QRect(16, 60, 114, 40))
        self.Calc.setStyleSheet("QPushButton {\n"
"    background-color: #0060E5;\n"
"    color: #FFFFFF;\n"
"    font-family: roboto;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius:4px;\n"
"   }\n"
"\n"
"")
        self.Calc.setProperty("operands", "")
        self.Calc.setObjectName("Calc")
        self.Graph = QtWidgets.QPushButton(self.keys)
        self.Graph.setGeometry(QtCore.QRect(130, 60, 114, 40))
        self.Graph.setStyleSheet("QPushButton {\n"
"    background-color: #2D3440;\n"
"    color: #FFFFFF;\n"
"    font-family: roboto;\n"
"    font-size: 14px;\n"
"   }\n"
"\n"
"")
        self.Graph.setProperty("operands", "")
        self.Graph.setObjectName("Graph")
        self.Menu = QtWidgets.QPushButton(self.keys)
        self.Menu.setGeometry(QtCore.QRect(240, 60, 114, 40))
        self.Menu.setStyleSheet("QPushButton {\n"
"    background-color: #2D3440;\n"
"    color: #FFFFFF;\n"
"    font-family: roboto;\n"
"    font-size: 14px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius:4px;\n"
"   }\n"
"\n"
"")
        self.Menu.setProperty("operands", "")
        self.Menu.setObjectName("Menu")
        self.inputs = QtWidgets.QTextEdit(self.keys)
        self.inputs.setGeometry(QtCore.QRect(16, 165, 346, 80))
        self.inputs.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inputs.setStyleSheet("QTextEdit {\n"
"background-color: #161A20;\n"
"color: #FFFFFF;\n"
"}")
        self.inputs.setObjectName("inputs")
        self.output = QtWidgets.QLineEdit(self.keys)
        self.output.setGeometry(QtCore.QRect(0, 260, 375, 48))
        self.output.setStyleSheet("QLineEdit {\n"
"background-color: #20252E;\n"
"color: #FFFFFF;\n"
"font-size: 24px;\n"
"font-weight: lighter;\n"
"}")
        self.output.setObjectName("output")
        self.inputs.raise_()
        self.division.raise_()
        self.equal.raise_()
        self.multiplication.raise_()
        self.minus.raise_()
        self.plus.raise_()
        self.AC.raise_()
        self.paranth.raise_()
        self.percent.raise_()
        self.nine.raise_()
        self.seven.raise_()
        self.eight.raise_()
        self.four.raise_()
        self.five.raise_()
        self.six.raise_()
        self.one.raise_()
        self.two.raise_()
        self.three.raise_()
        self.dot.raise_()
        self.zero.raise_()
        self.plusNminus.raise_()
        self.pushButton.raise_()
        self.Adv.raise_()
        self.clock.raise_()
        self.Calc.raise_()
        self.Graph.raise_()
        self.Menu.raise_()
        self.output.raise_()
        self.setCentralWidget(self.keys)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.division.setText(_translate("self", "÷"))
        self.equal.setText(_translate("self", "="))
        self.multiplication.setText(_translate("self", "x"))
        self.minus.setText(_translate("self", "–"))
        self.plus.setText(_translate("self", "+"))
        self.AC.setText(_translate("self", "AC"))
        self.paranth.setText(_translate("self", "( )"))
        self.percent.setText(_translate("self", "%"))
        self.nine.setText(_translate("self", "9"))
        self.seven.setText(_translate("self", "7"))
        self.eight.setText(_translate("self", "8"))
        self.four.setText(_translate("self", "4"))
        self.five.setText(_translate("self", "5"))
        self.six.setText(_translate("self", "6"))
        self.one.setText(_translate("self", "1"))
        self.two.setText(_translate("self", "2"))
        self.three.setText(_translate("self", "3"))
        self.dot.setText(_translate("self", "."))
        self.zero.setText(_translate("self", "0"))
        self.plusNminus.setText(_translate("self", "+/–"))
        self.pushButton.setText(_translate("self", "Trig"))
        self.Adv.setText(_translate("self", "Adv"))
        self.clock.setText(_translate("self", "clock"))
        self.Calc.setText(_translate("self", "Calculator"))
        self.Graph.setText(_translate("self", "Graph"))
        self.Menu.setText(_translate("self", "Menu"))
        self.inputs.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5(254)/3</p></body></html>"))
        self.output.setText(_translate("self", "19,134"))
        self.toolBar.setWindowTitle(_translate("self", "toolBar"))

        # Button Press Event 
##########################################################################################################    

        self.zero.clicked.connect(self.click_zero)
        self.one.clicked.connect(self.click_one)
        self.two.clicked.connect(self.click_two)
        self.three.clicked.connect(self.click_three)
        self.four.clicked.connect(self.click_four)
        self.five.clicked.connect(self.click_five)
        self.six.clicked.connect(self.click_six)
        self.seven.clicked.connect(self.click_seven)
        self.eight.clicked.connect(self.click_eight)
        self.nine.clicked.connect(self.click_nine)
        
        self.AC.clicked.connect(self.click_AC)
        self.plus.clicked.connect(self.click_plus)
        self.minus.clicked.connect(self.click_minus)
        self.multiplication.clicked.connect(self.click_multiplication)
        self.division.clicked.connect(self.click_division)
        self.dot.clicked.connect(self.click_dot)
        
##########################################################################################################  