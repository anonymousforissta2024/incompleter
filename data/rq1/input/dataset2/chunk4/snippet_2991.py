#Source: https://stackoverflow.com/questions/36967273/python3-attribute-error-type-object-mainwindow-qmainwindow-has-no-attribute
# Imports all the needed modules.
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Defines variables needed for the settings dialog.
currentDate = QtCore.QDate.currentDate()
maxDate = QtCore.QDate(2999, 12, 31)

class AppSettingsDialog(QtGui.QDialog): # The Settings dialog.
    def __init__(self, parent=None):
        # The initializer function for the dialog.
        super(AppSettingsDialog, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.calendarSpecificSettings()

        mainGridLayout = QtGui.QGridLayout()
        mainGridLayout.addWidget(self.calendarSpecificSettingsBox,
                                 0, 0)
        self.setLayout(mainGridLayout)

        self.exec_()

    def calendarSpecificSettings(self):
        # Creates a separator to put the widgets in.
        self.calendarSpecificSettingsBox = QtGui.QGroupBox(
            'Calendar Specific')

        self.maxDateLabel = QtGui.QLabel('Ma&ximum Date')
        self.maxDateEdit = QtGui.QDateEdit()
        self.maxDateEdit.setDisplayFormat('dd MMM yyyy')
        self.maxDateEdit.setDateRange(currentDate, maxDate)
        self.maxDateEdit.setDate(maxDate)
        self.maxDateLabel.setBuddy(self.maxDateEdit)
        self.maxDateEdit.dateChanged.connect(self.maximumDateChanged)
                    # Call to function error here ^

        self.calendarSpecificGridLayout = QtGui.QGridLayout()
        self.calendarSpecificGridLayout.addWidget(self.maxDateLabel,
                                                  0, 0)
        self.calendarSpecificGridLayout.addWidget(self.maxDateEdit,
                                                  0, 1)

        self.calendarSpecificSettingsBox.setLayout(
            self.calendarSpecificGridLayout)

    def maximumDateChanged(self, date): 
        MainWindow.calWidget.setMaximumDate(date)
        # ^This is the line that causes the error. I have multiple
        # 'MainWindow' calls - one for each of the settings I want
        # to change.

class MainWindow(QtGui.QMainWindow): # The main window.
    def __init__(self):
        # The initializer function for the window.
        super(MainWindow, self).__init__()
        mainMenu = self.menuBar()

        menuOptions = mainMenu.addMenu('Options')
        actionSettings = QtGui.QAction('Settings...', self)
        actionSettings.triggered.connect(self.appSettings)
        menuOptions.addAction(actionSettings)

        calWidget = QtGui.QCalendarWidget(self)
        calWidget.resize(300, 300)
        calWidget.setGridVisible(True)
        calWidget.setNavigationBarVisible(True)
        self.setCentralWidget(calWidget)

        self.statusBar().setSizeGripEnabled(True)
        self.statusBar().showMessage('Ready', 5000)

    def appSettings(self):
        # The function that invokes the dialog.
        AppSettingsDialog()

# One way to initialize the application.
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())