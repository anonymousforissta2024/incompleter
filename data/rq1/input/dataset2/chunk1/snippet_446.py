#Source: https://stackoverflow.com/questions/28116807/python3-pyqt5-nonetype-error-when-setting-value-in-radiobutton-connect
self.radioButton_1s.clicked.connect(self.setInterval(1))
self.radioButton_10s.clicked.connect(self.setInterval(10))
self.radioButton_any.clicked.connect(self.setInterval(0))