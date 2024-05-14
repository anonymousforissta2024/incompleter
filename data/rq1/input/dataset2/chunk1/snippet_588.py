#Source: https://stackoverflow.com/questions/44344818/socket-sendall-method-throws-typeerror-a-bytes-like-object-is-required-not
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("www.google.com")
mysock.connect(host, 80)
message = "GET / HTTP/1.1\r\n\r\n"
mysock.sendall(message)
data=mysock.recv(1000)
mysock.close()