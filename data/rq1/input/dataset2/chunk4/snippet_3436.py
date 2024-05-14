#Source: https://stackoverflow.com/questions/46989736/class-def-self-attributeerror-xx-object-has-no-attribute-xx
import hashlib
class Sicherheit:
    passwordFile = 'usercreds.tmp'
    def Signup(self):
        self.isSigned = False # !!! self.isSigned
        print("Sie müssen sich erst anmelden!\n")
        usernameInput = input("Bitte geben Sie Ihren Nutzername ein: \n")
        passwordInput = input("Bitte geben Sie Ihr Passwort ein: \n")
        usernameInputHashed = hashlib.sha512(usernameInput.encode())
        passwordInputHashed = hashlib.sha512(passwordInput.encode())

        with open(self.passwordFile, 'w') as f:
            f.write(str(usernameInputHashed.hexdigest()))
            f.write('\n')
            f.write(str(passwordInputHashed.hexdigest()))
            f.close()

        self.isSigned = True  # !!! self.isSigned
        print("Anmeldung war erfolgreich!\n")
        print("======================================================\n")
        self.Login()  # Moves onto the login def

    def Login(self):
        print("Sie müssen sich einloggen!\n")

        usernameEntry = input("Bitte geben Sie Ihren Nutzername ein: \n")
        passwordEntry = input("Bitte geben Sie Ihr Passwort ein: \n")
        usernameEntry = hashlib.sha512(usernameEntry.encode())
        passwordEntry = hashlib.sha512(passwordEntry.encode())
        usernameEntryHashed = usernameEntry.hexdigest()
        passwordEntryHashed = passwordEntry.hexdigest()

        with open(self.passwordFile) as r:
            info = r.readlines()
            usernameInFile = info[0].rstrip()
            passwordInFile = info[1].rstrip()

        if usernameEntryHashed == usernameInFile and passwordEntryHashed == passwordInFile:
            print("Anmeldung war erfolgreich!\n")

        else:
            print("Anmeldung war nicht erfolgreich!!!\n")
            self.Login()

    def CheckSign(self):
        if self.isSigned == True:  # !!! self.isSigned
            self.Login()
        else:
            self.Signup()
Kontrolle = Sicherheit()
Kontrolle.CheckSign()