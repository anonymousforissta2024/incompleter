#Source: https://stackoverflow.com/questions/27453945/where-is-this-typeerror-coming-from
#New User for EPM#
import os
import platform
import sys
from math import *
from PyQt4 import QtCore, QtGui
__version__ = '1.0.0'



class NewUser(QtGui.QDialog):
    def __init__(self, parent):
        super(NewUser, self).__init__(parent)

        self.initUi()

    def initUi(self):

        global name, email, setPass, passRepeat, nameEdit, emailEdit
        global setPassEdit, passRepeatEdit, ccIssueEdit, dbIssueEdit
        global pinEdit, ccIssueChkBx1, ccIssueChkBx2, adminChkBx
        global saveBtn, cancelBtn

        name = QtGui.QLabel('Name: ', self)
        email = QtGui.QLabel('Email: ', self)
        setPass = QtGui.QLabel('Set Password: ', self)
        passRepeat = QtGui.QLabel('Repeat Password', self)

        nameEdit = QtGui.QLineEdit(self)
        emailEdit = QtGui.QLineEdit(self)
        setPassEdit = QtGui.QLineEdit(self)
        passRepeatEdit = QtGui.QLineEdit(self)
        ccIssueEdit = QtGui.QLineEdit(self)
        dbIssueEdit = QtGui.QLineEdit(self)
        pinEdit = QtGui.QLineEdit('PIN', self)
        cvcEdit = QtGui.QLineEdit('CVC', self)

        ccIssueChkBx1 = QtGui.QCheckBox('Credit Card Issued', self)
        ccIssueChkBx2 = QtGui.QCheckBox('Debit Card Issued', self)
        adminChkBx = QtGui.QCheckBox('Make Admin', self)

        saveBtn = QtGui.QPushButton('Save and Close', self)
        cancelBtn = QtGui.QPushButton('Cancel', self)

        ui = QtGui.QGridLayout()

        ui.addWidget(name, 1, 0)
        ui.addWidget(email, 2, 0)
        ui.addWidget(setPass, 3, 0)
        ui.addWidget(passRepeat, 4, 0)
        ui.addWidget(nameEdit, 1, 1, 1, 4)
        ui.addWidget(emailEdit, 2, 1, 1, 4)
        ui.addWidget(setPassEdit, 3, 1, 1, 4)
        ui.addWidget(passRepeatEdit, 4, 1, 1, 4)
        ui.addWidget(ccIssueEdit, 5, 1, 1, 3)
        ui.addWidget(cvcEdit, 5, 4, 1, 1)
        ui.addWidget(dbIssueEdit, 6, 1, 1, 3)
        ui.addWidget(pinEdit, 6, 4, 1, 1)
        ui.addWidget(ccIssueChkBx1, 5, 0)
        ui.addWidget(ccIssueChkBx2, 6, 0)
        ui.addWidget(adminChkBx, 7, 4)
        ui.addWidget(saveBtn, 7, 0)
        ui.addWidget(cancelBtn, 7, 1)

        ccIssueChkBx1.stateChanged.connect(self.ccEn)
        ccIssueChkBx2.stateChanged.connect(self.dbEn)

        saveBtn.clicked.connect(self.save)

        self.ccEn()
        self.dbEn()

        self.setLayout(ui)
        self.resize(400, 300)
        self.center()
        self.show()

    def ccEn(self):

        if ccIssueChkBx1.isChecked():
            ccIssueEdit.setEnabled(True)
        else:
            ccIssueEdit.setEnabled(False)

    def dbEn(self):

        if ccIssueChkBx2.isChecked():
            dbIssueEdit.setEnabled(True)
            pinEdit.setEnabled(True)
        else:
            dbIssueEdit.setEnabled(False)
            pinEdit.setEnabled(False)

    def save(self, userName, userEmail, userPass, userCC=None, userCVC=None,
            userDB=None, userPin=None, isAdmin=False):

        userName = self.nameEdit.text()
        userEmail = self.emailEdit.text()

        if self.setPassEdit.text() == self.passRepeatEdit.text():
            userPass = self.setPassEdit.text()
        else:
            pass #Throw error here

        if self.ccIssueChkBx1.isChecked():
            if len(self.ccIssueEdit) == 15 and len(self.cvcEdit) == 4:
                userCC = self.ccIssueEdit.text()
                userCVC = self.cvcEdit.text()
                ccType = 'AMEX'
            elif len(self.ccIssueEdit) == 16 and len(self.cvcEdit) == 3:
                userCC = self.ccIssueEdit.text()
                userCVC = self.cvcEdit.text()
                ccType = 'MC/Visa'
            else:
                pass #Throw error here

        if self.ccIssueChkBx2.isChecked():
            if len(self.dbIssueEdit) == 16 and len(self.pinEdit) == 4:
                userDB = self.dbIssueEdit.text()
                userPin = self.pinEdit.text()
            else:
                pass #Throw error here

        if self.adminChkBx.isChecked():
            isAdmin = True

        userSave = newUser.Save(userName, userEmail, userPass, userCC, userCVC,
            ccType, userDB, userPin, isAdmin)

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



class Save(object):
    '''Creates a User Object'''

    def __init__(self, userName, userEmail, userPass, userCC, userCVC, ccType,
        userDB, userPin, isAdmin):

        self.create()

    def create(self):

        list = [userName, userEmail, userPass, userCC, userCVC, ccType, userDB,
            userPin, isAdmin]

        dirName = str(self.userName)
        os.mkdir(dirName)
        os.chdir(dirName)

        fileName = open('profile.txt', 'wb')
        for i in list:
            fileName.write(str(i))