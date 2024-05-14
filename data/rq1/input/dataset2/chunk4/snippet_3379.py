#Source: https://stackoverflow.com/questions/28817876/nameerror-name-record-is-not-defined-python-3
from socket import *
from codecs import decode
from chatrecord import ChatRecord
from threading import Thread
from time import ctime

class ClientHandler(Thread):

    def __init__(self, client, record):
        Thread.__init__(self)
        self._client = client
        self._record = record

    def run(self):
        self._client.send(bytes('Welcome', CODE))
        self._name = decode(self._client.recv(BUFSIZE), CODE)
        self._client.send(bytes(str(self._record), CODE))
        while True:
            message = decode(self._client.recv(BUFSIZE), CODE)
            if not message:
                print('Client disconnected')
                self._client.close()
                break
            else:
                message = self._name + '' + \
                          ctime() + '\n' + message
                self._record.add(message)
                self._client.send(bytes(str(self._record), CODE))


HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = 'ascii'
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('Waiting for connection...')
    client, address = server.accept()
    print('...connected from:', address)
    handler = ClientHandler(client, record)
    handler.start()