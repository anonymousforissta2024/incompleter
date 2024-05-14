#Source: https://stackoverflow.com/questions/74934265/python-threading-typeerror-too-many-arguments
import threading

class ReadWrite:
    threadList = [0] * 20

    def __init__(self, origData):
        self.readerLock = threading.Lock()
        self.writerLock = threading.Lock()
        self.data = origData
        self.readerCount = 0

    def acquireReadLock(self):
        self.readerLock.acquire()

    def releaseReadLock(self):
        self.readerLock.release()

    def acquireWriteLock(self):
        self.writerLock.acquire()

    def releaseWriteLock(self):
        self.writerLock.release()

    def printData(self, threadName):
        print(threadName, ' printed ', self.data)

    def modifyData(self, threadName, newData):
        print(threadName, ' changed ', self.data, ' to ', newData)
        self.data = newData
    
    def run(self):
        for x in range(20):
            threadString = 'Thread' + str(x)
            if x % 6:
                self.threadList[x] = threading.Thread(target=self.printData, args=(threadString))
            else:
                newData = self.data + str(x)
                self.threadList[x] = threading.Thread(target=self.modifyData, args=(threadString, newData))
            self.threadList[x].start()

        for x in range(20):
            self.threadList[x].join()
myVar = ReadWrite('Hello')
myVar.run()