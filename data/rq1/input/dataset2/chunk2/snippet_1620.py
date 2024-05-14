#Source: https://stackoverflow.com/questions/50712783/pyqt5-how-to-display-list-in-qmessagebox-typeerror-argument-3-has-unexpected
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'List manipulation'
        self.left = 10
        self.top = 10
        self.width = 325
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 200)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 230)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        xlist = textboxValue.splitlines()
        xlist_final=[]
        for xitem in xlist:
            if xitem.find("abc") != -1:
                xlist_final.append(xitem)
    QMessageBox.question(self, 'List manipulation', xlist_final, QMessageBox.Ok, QMessageBox.Ok)
    self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())