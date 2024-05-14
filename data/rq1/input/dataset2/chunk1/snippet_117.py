#Source: https://stackoverflow.com/questions/49163393/twisted-python3-typeerror-init-missing-1-required-positional-argument
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.internet import task
from twisted.internet import protocol

#from screenhelp import ScreenHelp ** Not relevant to error


class Screen(Protocol):

    def __init__(self, factory):
        self.factory = factory
        self.connection = False
        self.loop = task.LoopingCall(screenRefresh)
        self.loopDeferred = None
        self.stack = []
        self.cs = ScreenHelp()

    def connectionMade(self):
        self.loopDeferred = self.loop.start(self,5)

    def connectionLost(self, reason):
        self.loop.stop(self)

    def dataReceived(self, data):
        self.stack.append(data)

    def screenRefresh(self):

        #self.transport.write(self.cs.clr()) ** Not relevent - issues clear screen command.
        for x in self.stack:
            self.transport.write(x)

class ScreenFactory(Factory):
    def buildProtocol(self, addr):
        return Screen()


def main():
    endpoint1 = TCP4ServerEndpoint(reactor, 64000)
    endpoint1.listen(ScreenFactory)
    reactor.listenTCP(5000, fact)
    reactor.run()


if __name__ == "__main__":
     main()