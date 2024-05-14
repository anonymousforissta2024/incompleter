#Source: https://stackoverflow.com/questions/53824369/script-working-fine-while-it-should-raise-nameerror
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pynput.keyboard import Key, Listener
from itertools import combinations

import sys
import re

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        ##BELOW DETECTS WHEN THE USER PRESS ENTER
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()                               
        self.listener1 = Listener(on_press=self.on_press_top)

        ##CENTERING THE SCREEN
        def center(self):
            qr = QMainWindow.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

        ##JUST GUI
        self.setWindowTitle("Foo")
        self.setFixedSize(950, 710)
        self.setStyleSheet("background-color: rgb(119,136,153)")
        QApplication.setOverrideCursor(Qt.PointingHandCursor)

        ##SET -LINE EDIT
        self.kume_edit = QLineEdit(self)
        self.kume_edit.setText("{")
        self.kume_edit.setStyleSheet("QLineEdit{ background-color: orange; color: blue; font: 11 }")

        fnt = self.kume_edit.font()
        fnt.setPointSize(15)
        self.kume_edit.setFont(fnt)
        self.kume_edit.setGeometry(140, 300, 300, 30)
        ##

        ##SET -LABEL
        self.kume_label = QLabel(self)
        self.kume_label.setText("SET:")
        self.kume_label.setStyleSheet("QLineEdit{ background-color: orange; color: blue; font: 11 }")

        fnt1 = self.kume_label.font()
        fnt1.setPointSize(15)
        self.kume_label.setFont(fnt1)
        self.kume_label.setGeometry(50, 300, 60, 32)
        ##

        ##TOPOLOGY -LINE EDIT
        self.top_edit = QLineEdit(self)
        self.top_edit.setText("{{")
        self.top_edit.setStyleSheet("QLineEdit{ background-color: orange; color: blue; font: 11 }")

        fnt2 = self.top_edit.font()
        fnt2.setPointSize(15)
        self.top_edit.setFont(fnt2)
        self.top_edit.setGeometry(140, 400, 300, 30)
        ##

        ##TOPOLOGY -LABEL
        self.topo_label = QLabel(self)
        self.topo_label.setText("TOP:")
        self.topo_label.setStyleSheet("QLineEdit{ background-color: orange; color: blue; font: 11 }")

        fnt3 = self.topo_label.font()
        fnt3.setPointSize(15)
        self.topo_label.setFont(fnt3)
        self.topo_label.setGeometry(50, 400, 80, 32)
        ##

        ##FUNCTION CHANGES THIS LABEL WHEN THE DESIRED CONDITION OCCURS
        self.top_label = QLabel(self)
        fnt4 = self.top_label.font()
        fnt4.setPointSize(15)
        self.top_label.setFont(fnt4)
        self.top_label.setGeometry(140, 450, 900, 30)
        ##

        ##BUTTON SHOWS THAT THE PROGRAM WORKING FINE
        ##CLICK THIS BUTTON BEFORE AND AFTER YOU RUN
        but = QPushButton(self)
        but.setGeometry(500,400,50,50)
        but.setText("Click Me")
        but.clicked.connect(self.but_test)
        self.count_test = 0
        ##

        self.top_ = 0
        self.kord_ = 300

        self.show()

    def but_test(self):             #########CLICK THIS BUTTON
        self.count_test += 1        #########TO SEE THAT ITS WORKING AFTER 'print(type(y))' PART
        self.top_label.setText("The program working fine {}".format(self.count_test))

    def on_press(self,key): #########THIS DETECTS WHEN THE USER PRESS "ENTER" IN 'SET QLINEEDIT'

        if key == Key.enter:


            if self.kume_edit.text()[-1] == ",":
                self.kume_edit.setText(self.kume_edit.text()[:-1] + "}")
                self.kume_edit.setReadOnly(True)
                self.listener1.start()
                self.listener.stop()

            else:
                self.kume_edit.setText(self.kume_edit.text() + ",")


    def on_press_top(self,key): #########THIS DETECTS WHEN THE USER PRESS "ENTER" IN 'TOPOLOGY QLINEEDIT'

        if key == Key.enter:
            self.top_ += 15

            if self.top_ > 220:
                self.kord_ += 15
                self.top_edit.setGeometry(140, 400, self.kord_, 30)

            if self.top_edit.text()[-1] == "{":
                self.top_edit.setText(self.top_edit.text()[:-2])
                self.top_edit.setText(self.top_edit.text() + "}")
                self.top_edit.setReadOnly(True)

                self.top_edit.setGeometry(140, 400, self.kord_, 30)

                self.topoloji_mi()  #####################HERE THE FUNCTION IS CALLED - ONLY HERE

                self.listener1.stop()

            elif self.top_edit.text()[-1] == ",":
                self.top_edit.setText(self.top_edit.text()[:-1] + "}")
                self.top_edit.setText(self.top_edit.text() + ",")
                self.top_edit.setText(self.top_edit.text() + "{")

            else:
                self.top_edit.setText(self.top_edit.text() + ",")


    def kumetop(self): #############THIS JUST RETURNS TWO LISTS
        reg = r"\{(.*?)\}"
        matches = re.findall(reg, self.top_edit.text()[1:-1])

        top_set = []
        top_set.append(set())
        for x in matches:
            top_set.append(set(x.split(",")))

        kume_set = []
        for x in self.kume_edit.text():
            if x.isalnum():
                kume_set.append(set(x.split(",")))
        return kume_set,top_set

    def topoloji_mi(self): #################PROB FUNCTION #######################################
        kume_set,top_set = self.kumetop() ###TAKING THE LISTS


        for x in combinations(top_set, 2):

            ################WHATS THIS
            print ("IM A PRINT FUNCTION WORKING FINE") ###THIS PRINT WORKS
            print(list(y))
            del list(y)[0]               #######PYCHARM RAISE NO ERROR, WINDOW IS ALSO WORKING
            print (type(y))              ###CLICK THE TEST BUTTON

            if len(z) == len(list(y)) and all([z.count(i) == list(y).count(i) for i in kume_set]):
                self.top_label.setText("BLABLABLA")
                print("IM NOT WORKING")



    def close_application(self):
        sys_exit()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()