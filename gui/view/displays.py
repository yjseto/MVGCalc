from typing import Optional

from PyQt5.QtWidgets import *

import pyqtgraph as pg
import numpy as np
from lib.enums.base import UnitEnum
from lib.enums.converter_enums import Length, Measure
from lib.enums.keys import ActionKey
from lib.models.result import GraphResult, ResultBase

from gui.components.textarea import MvgCalcExpressionTextField
from gui.containers.app import MvgCalcApplication
from gui.containers.controller import KeyInputController
from gui.screen.graph import GraphScreen
from gui.screen.unit_converter import UnitConverter
from gui.screen.unit_listboxes.measures_listbox import measuresListbox
from gui.screen.unit_listboxes.length_listbox import legnthListbox
from gui.screen.unit_listboxes.weight_listbox import weightListbox

"""
    IMPORTANT: reciever for signal from keyboard when signal is returned the  
    retrieve_updated_user_input_object method is invoked.
"""
class MvgCalcDisplayBase(QWidget):
    def __init__(self, app : MvgCalcApplication):
        super().__init__()
        self.app = app

        #create vertical box structure to place widget components
        self.layout_main = QVBoxLayout()
        self.layout_main.setContentsMargins(2, 0, 2, 0)

        self.textfield_expression = MvgCalcExpressionTextField()
        self.keyboard = KeyInputController(self.app)

        self.keyboard.refresh_expr_screen.connect(self.refresh_expr_screen)  

    def refresh_expr_screen(self, action : Optional[ActionKey] = None):

        if action == ActionKey.UP or action == ActionKey.DOWN:
            self.app.user_input = self.keyboard.hist_expr_display.hist_expr_listbox.update(action)
            self.textfield_expression.setText(self.app.user_input.format_usr_inp_expr_as_str(True))
        else:
            self.app.h_pos = self.textfield_expression.update(self.app.user_input, action)

class BasicCalcDisplay(MvgCalcDisplayBase):
    def __init__(self, app : MvgCalcApplication):
        super().__init__(app)
        
        self.display_result_text = QTextEdit()
        self.display_result_text.setReadOnly(True)
        
        self.display_expression_text = MvgCalcExpressionTextField()
        
        self.keyboard.return_result.connect(self.retrieve_result_object)  

        self.layout_main.addWidget(self.display_result_text)
        self.layout_main.addWidget(self.textfield_expression)
        self.layout_main.addWidget(self.keyboard)

        self.setLayout(self.layout_main)

    def retrieve_result_object(self, result : ResultBase):
        if result.success == False:
            self.display_result_text.setText(result.get_formatted_error_msg_list())
        else:
            self.display_result_text.setText(result.value)
            self.textfield_expression.setText(result.expression)


'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''

class GraphDisplay(MvgCalcDisplayBase):
    def __init__(self, app : MvgCalcApplication):
        super().__init__(app)

        self.x = np.linspace(-100,100,3000)
        self.graph_config = {'x': self.x,
                             'np': np, 
                             'sin': np.sin, 
                             'cos': np.cos, 
                             'tan': np.tan,
                             'asin': np.arcsin,
                             'acos': np.arccos,
                             'atan':np.arctan,
                             'log': np.log10,
                             'ln' : np.emath.log}
        #support for additional functions can be added to this dictionary
        self.pen = pg.mkPen(color = 'w', width = 1.5) #sets the style of the line we plot on the graph

        self.graph_screen = GraphScreen()

        self.keyboard.return_result.connect(self.retrieve_result_object)
        self.keyboard.clear_graph.connect(self.clear_graph_screen)

        self.layout_main.addWidget(self.graph_screen)
        self.layout_main.addWidget(self.textfield_expression)
        self.layout_main.addWidget(self.keyboard)

        self.setLayout(self.layout_main)
    
    def clear_graph_screen(self):
        self.graph_screen.clear()

    def retrieve_result_object(self, result : GraphResult):

        if result.success == True:
            #x = result.x
            #y = eval(result.y)
            y = eval(result.y, self.graph_config)
            self.graph_screen.plot(self.x,y,pen = self.pen)
        else:
            print(result.error_msgs[0])
            
class UnitConvDisplay(MvgCalcDisplayBase):
    def __init__(self, app : MvgCalcApplication):
        super().__init__(app)
        
        self.unit_conv_window = UnitConverter()
        #self.display_expression_text = MvgCalcExpressionTextField()
        self.current_measure = Measure.LENGTH
        self.unit_1 = Length.METER
        self.unit_2 = Length.KILOMETER

        self.keyboard.return_result.connect(self.retrieve_result_object)  
        self.unit_1_text = self.unit_conv_window.ui.unit_1 #textfield will be unit_1 text edit area
        self.unit_2_text = self.unit_conv_window.ui.unit_2
        self.measures_listbox = measuresListbox()
        self.length_listbox = legnthListbox()
        self.weight_listbox = weightListbox()
        #self.layout_main.addWidget(self.unit_conv_window)
        #self.layout_main.addWidget(self.textfield_expression)
        #self.layout_main.addWidget(self.keyboard)

        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(self.unit_conv_window)
        self.stacked_widget.addWidget(self.measures_listbox)
        self.stacked_widget.addWidget(self.length_listbox)
        self.stacked_widget.addWidget(self.weight_listbox)

        self.layout_main.addWidget(self.stacked_widget)
        self.layout_main.addWidget(self.keyboard)
        self.setLayout(self.layout_main)

        self.unit_conv_window.display_listbox.connect(self.switch_window_measure)
        self.measures_listbox.switch_window.connect(self.switch_window_measure)
        self.measures_listbox.current_measure.connect(self.set_cur_measure)


        self.unit_conv_window.display_units_1.connect(self.switch_window_units_1)
        self.unit_conv_window.display_units_2.connect(self.switch_window_units_2)

        #for switching back to normal
        self.length_listbox.switch_window_1.connect(self.switch_window_units_1)
        self.weight_listbox.switch_window_1.connect(self.switch_window_units_1)

        self.length_listbox.switch_window_2.connect(self.switch_window_units_2)
        self.weight_listbox.switch_window_2.connect(self.switch_window_units_2)

        #Set length units
        self.length_listbox.unit_1.connect(self.set_unit_1)
        self.length_listbox.unit_2.connect(self.set_unit_2)

        #set width units
        self.weight_listbox.unit_1.connect(self.set_unit_1)
        self.weight_listbox.unit_2.connect(self.set_unit_2)

        self.keyboard.refresh_expr_screen.connect(self.refresh_expr)  
        
        #need a stacked layout here
        #also need a pyqt signal from the UnitConverter class


    def refresh_expr(self, action : Optional[ActionKey] = None): #will have to modify this to make it connect to unit 1 and keyboard
        self.app.h_pos = self.unit_1_text.update(self.app.user_input, action)
        self.app.h_pos = self.unit_2_text.convert(self.app.user_input,self.current_measure, self.unit_1, self.unit_2)
        #immediately evaluate for unit 2 and insert the number
        #like some util file, custom enum -> string -> eval to number -> convert -> display
    
    def set_cur_measure(self, measure: Measure): #sets what we are measuring based on what was clicked
        #print(measure)
        self.current_measure = measure
    
    def set_unit_1(self,unit: UnitEnum):
        self.unit_1 = unit
        #print(f"Unit 1: {self.unit_1}")
    
    def set_unit_2(self,unit: UnitEnum):
        self.unit_2 = unit
        #print(f"Unit 2: {self.unit_2}")


    def switch_window_measure(self):
        cur_index = self.stacked_widget.currentIndex()

        if cur_index == 0:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(0)

        self.unit_conv_window.ui.measures_listbox.setText(self.current_measure.textSymbol)
        
    def switch_window_units_1(self):
        cur_index = self.stacked_widget.currentIndex()
        self.length_listbox.target = 1 #now we're setting unit_1
        self.weight_listbox.target = 1

        if cur_index == 0:
            if self.current_measure == Measure.LENGTH:
                self.stacked_widget.setCurrentIndex(2)
            elif self.current_measure == Measure.WEIGHT:
                self.stacked_widget.setCurrentIndex(3)
        else:
            self.stacked_widget.setCurrentIndex(0)

        self.unit_conv_window.ui.unit_listbox_1.setText(self.unit_1.symbol)
    
    def switch_window_units_2(self):
        cur_index = self.stacked_widget.currentIndex()
        self.length_listbox.target = 2 #say now we're setting unit_2
        self.weight_listbox.target = 2

        if cur_index == 0:
            if self.current_measure == Measure.LENGTH:
                self.stacked_widget.setCurrentIndex(2)
            elif self.current_measure == Measure.WEIGHT:
                self.stacked_widget.setCurrentIndex(3)
        else:
            self.stacked_widget.setCurrentIndex(0)

        self.unit_conv_window.ui.unit_listbox_2.setText(self.unit_2.symbol)

    def retrieve_result_object(self, result : ResultBase):
        pass
        '''if result.success == False:
            error_str = ""
            for error in result.error_msgs:
                error_str = error_str + str(error) + '\n'    
            self.display_result_text.setText(error_str)
        else:
            self.display_result_text.setText(result.value)
            self.textfield_expression.setText(result.expression)'''