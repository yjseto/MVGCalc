from pyqtgraph import PlotWidget

'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''
class GraphScreen(PlotWidget):
    def __init__(self, plotItem=None):
        super().__init__(plotItem)
        self.showGrid(x = True, y =True)
        self.setXRange(-30, 30, padding=0)
        self.setYRange(-30, 30, padding=0)
        

        
        
