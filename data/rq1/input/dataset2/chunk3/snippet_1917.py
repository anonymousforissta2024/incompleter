#Source: https://stackoverflow.com/questions/52345457/pyqt4-problems-with-resorce-system-typeerror-qregisterresourcedata
import sys                              
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

mainwindow = uic.loadUiType("mainmenu2.ui")[0] #load the UI
class Mainmenu(QtGui.QMainWindow, mainwindow):
    def __init__(self, parent=None):
        super(Mainmenu, self).__init__(parent)
        self.setupUi(self)
        #self.aboutp.clicked.connect(self.linkabout)

app = QtGui.QApplication(sys.argv)
mainwindow = Mainmenu
#aboutwindow = About_us_page(None)
mainwindow.show()
app.exec_()