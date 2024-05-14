#Source: https://stackoverflow.com/questions/53632379/attributeerror-builtin-function-or-method-object-has-no-attribute-addlayout
class UIWidget(QtWidgets.QWidget):    
    def __init__(self, parent=None):
        super(UIWidget, self).__init__(parent)        
        # Initialize tab screen
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()        

        # Add tabs
        self.tabs.addTab(self.tab1, "Face")

        self.display = PlayStreaming()
        # Create first tab
        self.createGridLayout()
        self.tab1.layout = QtWidgets.QVBoxLayout()
        self.tab1.layout.addWidget(self.display, stretch=1)
        self.tab1.layout.addWidget(self.horizontalGroupBox)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.tabs)

    def createGridLayout(self):
        hlay1 = QtWidgets.QVBoxLayout()   
        self.horizontalGroupBox = QtWidgets.QGroupBox("")
        self.horizontalGroupBox.setStyleSheet("QGroupBox{ background-color: red; border: none;}")          
        self.ScaleUpButton=QtWidgets.QPushButton('ScaleUp')
        self.ScaleUpButton.clicked.connect(self.display.scaleupSignal)
        hlay1.addWidget(self.ScaleUpButton) 
        self.ScaleDownButton=QtWidgets.QPushButton('ScaleDown')
        self.ScaleDownButton.clicked.connect(self.display.scaledownSignal)
        hlay1.addWidget(self.ScaleDownButton) 
        self.resetButton=QtWidgets.QPushButton('Reset')
        hlay1.addWidget(self.resetButton)
        self.resetButton.clicked.connect(self.display.resetallarraysSignal)
        self.RecognizeButton=QtWidgets.QPushButton('Recognize')
        self.RecognizeButton.clicked.connect(self.display.send_signal)
        hlay1.addWidget(self.RecognizeButton)             
        self.layout.addLayout(hlay1)
        self.horizontalGroupBox.setLayout(self.layout)