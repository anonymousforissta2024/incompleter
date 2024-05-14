#Source: https://stackoverflow.com/questions/45897118/attribute-error-python-from-a-new-file
import utils
import sys


TOTAL_ROOMS = 500
rooms = []
suite = []
reservations = []
reservationParts = []
roomNum = 0
suiteOut = ""
suiteF = ""
name = ""
userInput = ""
suiteT = " and is a suite"
utils.users.append("foo:hello")


userInput = input(">>> ")
while True:
        if userInput == "new -r":
                utils.username = input("admin$ -u>>> ")
                utils.password = input("admin$ -p>>> ")
                utils.credentials = utils.username + ":" + utils.password
                if utils.isUser(credentialsInput=utils.credentials):
                        userInput = input("rsr# -n ")
                        reservationParts = userInput.split()
                        roomNum = reservationParts[0]
                        name = reservationParts[1]
                        if name in rooms:
                                print(">>> Room is occupied")
                        elif name in utils.roomName:
                                print(">>> Room is occupied")
                        rooms.append(roomNum)
                        utils.roomName.append(name)
                        utils.loopCount = 0
                        if "--suite" in userInput:
                                suite.append(True)
                                suiteOut = suiteT
                        else:
                                suite.append(False)
                                suiteOut = suiteF
                        reservations.append("Room " + roomNum + " is filled by " +
                                            utils.roomName.__getitem__(utils.loopCount) + suiteOut)
                        for ints in rooms:
                                if suite.__getitem__(utils.loopCount):
                                        suiteOut = suiteT
                                else:
                                        suiteOut = suiteF
                                sys.stdout.write("Room " + ints + " is filled by " +
                                                 utils.roomName.__getitem__(utils.loopCount) + suiteOut)
                                print()
                                utils.loopCount += 1
                        userInput = input(">>> ")
                        if userInput == "quit()":
                                break
                else:
                        print("Invalid Credentials")
        elif userInput == "new -u":
                if utils.runCredentialCheck():
                    utils.username = input("new -u -u>>> ")
                    utils.password = input("new -u -p>>> ")
                    utils.registerUser(creds=(utils.username + ":" + utils.password))
                else:
                    print("Invalid Credentials")
                userInput = input(">>> ")