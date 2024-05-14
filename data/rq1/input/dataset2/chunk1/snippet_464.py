#Source: https://stackoverflow.com/questions/34562737/attributeerror-using-pyqt4
import sys
from PyQt4 import QtGui,QtCore
class Line(QtGui.QWidget):
    def __init__(self):
        super(Line,self).__init__()
        self.x1=-1
        self.x2=-1
        self.y1=-1
        self.y2=-1
        self.initUI()

    def initUI(self):

        b1=QtGui.QPushButton("Draw Line",self)
        b1.setGeometry(250,25,100,30)
        b1.clicked.connect(self.repaint)
        l1=QtGui.QLabel("x1 :",self)
        l2=QtGui.QLabel("x2 :",self)
        l3=QtGui.QLabel("y1 :",self)
        l4=QtGui.QLabel("y2 :",self)
        l5=QtGui.QLabel(self)
        l1.setGeometry(100,250,100,100)
        l2.setGeometry(250,250,100,100)
        l3.setGeometry(100,350,100,100)
        l4.setGeometry(250,350,100,100)
        l5.setGeometry(1000,1000,1000,1000)
        self.x_1=QtGui.QLineEdit(self)
        self.x_2=QtGui.QLineEdit(self)
        self.y_1=QtGui.QLineEdit(self)
        self.y_2=QtGui.QLineEdit(self)
        self.x_1.setGeometry(130,275,100,50)
        self.x_2.setGeometry(280,272,100,50)
        self.y_1.setGeometry(130,375,100,50)
        self.y_2.setGeometry(280,375,100,50)
        self.r1=QtGui.QRadioButton("Thin Line",self)
        self.r1.move(100,25)
        self.r2=QtGui.QRadioButton("Thick Line",self)
        self.r2.move(100,55)
        self.r3=QtGui.QRadioButton("Dotted Line",self)
        self.r3.move(100,85)
        self.setGeometry(150,150,500,500)
        self.setWindowTitle("Line")
        self.show()

    def paintEvent(self,e):
        self.qp=QtGui.QPainter()
        self.qp.begin(self)
        self.draw(self.qp)
        self.qp.end()

    def draw(self,qp):
        self.x1=self.x_1.text().toInt()[0]
        self.x2=self.x_2.text().toInt()[0]
        self.y1=self.y_1.text().toInt()[0]
        self.y2=self.y_2.text().toInt()[0]

        pen=QtGui.QPen(QtCore.Qt.black,1)
        pen.setStyle(QtCore.Qt.SolidLine)

        if self.r1.isChecked():
            pen.setStyle(QtCore.Qt.SolidLine)
        if self.r2.isChecked():
            pen.setWidth(2)
        if self.r3.isChecked():
            pen.setStyle(QtCore.Qt.DashLine)
        qp.setPen(pen)

        qp.drawLine(self.x1,self.y1,self.x2,self.y2)

def main():
    app=QtGui.QApplication(sys.argv)
    l1=Line()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()