#Source: https://stackoverflow.com/questions/61128279/pyside2-how-to-unassign-current-layout-and-assign-a-new-one-to-a-window-widget
import sys
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program")
        self.setGeometry(300, 300, 300, 300)
        self.start()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def start(self):
        self.startbutton = QPushButton("Start App")

        layout = QVBoxLayout()
        layout.addWidget(self.startbutton)

        self.setLayout(layout)

        self.startbutton.clicked.connect(self.home)

    def home(self):
        self.clearLayout(self.layout)
        self.message=QLabel("Welcome to homepage")
        layout=QVBoxLayout()
        layout.addWidget(self.message)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window=Window()
    window.show()
    sys.exit(app.exec_())