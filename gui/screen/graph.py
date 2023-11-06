
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget

'''
Similar to basic But i just replaced the top with the graph instead of the resulting string
just for now
'''
class GraphScreen(PlotWidget):
    def __init__(self, plotItem=None):
        super().__init__(plotItem)
        #I hope to be able to do most of the graph styling here
        #can customize look here?
        styles = {'color':'white', 'font-size':'20px'}
        self.showGrid(x = True, y =True)
        #self.pen = pg.mkPen(color = 'w', width = 1.5)
        #self.plot(y=0,pen = self.pen) trying to draw axis lines
        #can set the x and y range in this object
        #might be messed up
        #x = sp.Symbol('x')
        self.setXRange(-30, 30, padding=0)
        self.setYRange(-30, 30, padding=0)
        #self.transformations = {'x': x, 'np': np, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,'asin': np.arcsin,'acos': np.arccos,'atan':np.arctan}
        

        
        
