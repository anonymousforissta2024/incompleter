#Source: https://stackoverflow.com/questions/70637794/typeerror-when-using-af-inet-in-the-sockets-library
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(socket.gethostname())
print("client successfully started")
msg = s.recv(1024)
print(msg.decode("utf-8"))