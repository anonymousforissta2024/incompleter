#Source: https://stackoverflow.com/questions/67369750/attributeerror-socket-object-attribute-send-is-read-only
import socket

target_host = "google.com"

target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))


client.send = ("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)