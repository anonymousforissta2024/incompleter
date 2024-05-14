#Source: https://stackoverflow.com/questions/28116807/python3-pyqt5-nonetype-error-when-setting-value-in-radiobutton-connect
@QtCore.pyqtSlot()
def setInterval(self,i):

    if i == 1:
        n = 1/self.doubleSpinBox_TimeIndexStep.value() #TODO: use math.floor/ceiling to geht integers
        self.spinBox_CopyInterval.setEnabled
        self.spinBox_CopyInterval.setValue(n)
    elif i == 10:
        n = 10/self.doubleSpinBox_TimeIndexStep.value()
        self.spinBox_CopyInterval.setEnabled
        self.spinBox_CopyInterval.setValue(n)