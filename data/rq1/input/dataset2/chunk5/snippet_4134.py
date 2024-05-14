#Source: https://stackoverflow.com/questions/59036061/how-to-fix-typeerror-while-plotting-using-pyqtgraph
import pyqtgraph as pg
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from Ui_GraphicsLayout import Ui_GraphicsLayout #pyqt layout class that configures the graph window

class Polar(QMainWindow):

    def __init__(self, title = "Time Domain Plot", name = "Channel"):
        super().__init__()

        pg.setConfigOption('background', 'w')

        self.__ui = Ui_GraphicsLayout()
        self.__ui.setupUi(self)

        self.setWindowTitle("Measurement System - {:s}".format(title))

        self.__plot = self.__ui.widget.addPlot(title = name, row = 0, col = 0);
        self.__pditem = self.__plot.plot(pen=None, symbol = 'o', symbolSize=5)

        self.__plot.setAspectLocked()
        self.__plot.addLine(x=0, pen=0.2)
        self.__plot.addLine(y=0, pen=0.2)

    def plot(self, data1, data2):  
        self.__pditem.setData(data1,data2)