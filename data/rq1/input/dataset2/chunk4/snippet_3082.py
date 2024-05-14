#Source: https://stackoverflow.com/questions/36404680/nameerror-name-is-not-defined-for-user-input
class user:
    def __init__(self, usrName, pWord):
        self.usrName = usrName
        self.pWord = pWord

    def createUsrPw(self):
        f = open("usrName.txt", "a")
        f.write(usrName)
        f.write("   ")
        f.write(pWord)
        f.write("\n")
        f.close()


usr1 = user("Ben", "testPw")

usr1.createUsrPw()