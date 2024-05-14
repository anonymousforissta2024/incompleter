#Source: https://stackoverflow.com/questions/58075064/sock-bind-typeerror-an-integer-is-required
import socket
UDP_IP="localhost"
UDP_PORT="8080"
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))