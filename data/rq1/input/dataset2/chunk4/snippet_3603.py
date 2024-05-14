#Source: https://stackoverflow.com/questions/45897118/attribute-error-python-from-a-new-file
import runMain


def isUser(credentialsInput):
    return credentialsInput in runMain.users


def isReserved(names):
    for strings in runMain.roomName:
        if names in strings:
            return True
        else:
            return False


def getIndex(e, check):
    return e.index(check)


def findInArray(e, searchName):
    runMain.i = 0
    while runMain.i < len(e):
        test = e[runMain.i]
        if searchName in test:
            break
    return runMain.i


def registerUser(creds):
    runMain.users.__add__(len(runMain.users), creds)


def runCredentialCheck():
    runMain.username = input("admin$ -u>>> ")
    runMain.password = input("admin$ -p>>> ")
    runMain.credentials = runMain.username + ":" + runMain.password
    return isUser(runMain.credentials)