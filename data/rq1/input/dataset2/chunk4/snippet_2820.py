#Source: https://stackoverflow.com/questions/18831771/pyqt4-signal-attributeerror-object-has-no-attribute
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class StringListDlg(QDialog):

    def __init__(self, name, strings, parent=None):
        super(StringListDlg, self).__init__(parent)

        self.listWidget = QListWidget()
        self.listWidget.addItems(strings)
        addButton = QPushButton("&Add...")

        grid = QGridLayout()
        grid.addWidget(self.listWidget, 0, 0, 7, 1)

        self.setLayout(grid)
        self.setWindowTitle("Edit {} List".format(name))

        self.connect(addButton, SIGNAL("clicked()"), self.add)

        def add(self):
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StringListDlg("Fruit", ['apples', 'bananas'])
    form.exec_()