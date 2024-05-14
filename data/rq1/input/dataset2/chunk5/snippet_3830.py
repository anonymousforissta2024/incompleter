#Source: https://stackoverflow.com/questions/45154163/attributeerror-second-object-has-no-attribute-funct
class Second(QDialog):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        def funct():
            print("This is a test")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel, self)
        buttonBox.rejected.connect(self.reject)
        buttonBox.accepted.connect(self.funct)