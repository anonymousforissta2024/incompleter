#Source: https://stackoverflow.com/questions/50046578/i-understad-why-i-get-typeerror-getsockaddrarg-af-inet-address-must-be-tuple
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 5005

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + " Port: " + str(server_port))
sock.connect(('0.0.0.0', 5002))
while True:
    client_address = ('0.0.0.0')
    status = 'ok'
    print("Echoing back "+ str(status) + " to " + str(client_address))
    sen = sock.sendto(status.encode(),client_address)