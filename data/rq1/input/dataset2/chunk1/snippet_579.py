#Source: https://stackoverflow.com/questions/47044129/nameerror-name-self-is-not-defined-after-using-eval
class MyApp(QMainWindow):
    def __init__(self):
            [...]
            Schaltpunkte=["Aussen1","Innen1","Innen2","Innen","Alle"]
            for Schaltpunkt in Schaltpunkte:
                 eval("self.ui.Button_"+Schaltpunkt+"Laden.clicked.connect(lambda: self.ladeZeitschaltung("+Schaltpunkt+"))")