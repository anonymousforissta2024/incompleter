#Source: https://stackoverflow.com/questions/50995772/python3-socket-attributeerror-io-bufferedreader-object-has-no-attribute-en
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5460

def myC_F():

    try:
        s.connect((host, port))
        print("connected to socket")
    except:
        print("failed connecting to: ", host, port)

    fPath = input("Enter file to send:> ")
    fSize = os.path.getsize(fPath)
    fSize = str(fSize)
    s.send(fSize.encode())
    print("...DONE SENDING SIZE :", fSize)
    while True:
        with open(fPath, "rb") as f:
            s.sendall(f.encode())


myC_F()