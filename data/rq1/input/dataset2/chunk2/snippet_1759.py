#Source: https://stackoverflow.com/questions/18613839/python-nameerror-when-defining-class
class NetVend:
    def blankCallback(data):
        pass

    def sendCommand(command, callback=NetVend.blankCallback):
        return NetVend.sendSignedCommand(command, NetVend.signCommand(command), callback)

    def sendSignedCommand(command, signature, callback):
        pass