#Source: https://stackoverflow.com/questions/50046578/i-understad-why-i-get-typeerror-getsockaddrarg-af-inet-address-must-be-tuple
import echoUDP

serveraddress = '0.0.0.0'
serverport = 5002

server2 = (server_address, server_port)
s.bind(server2)
print("Listening on " + server_address + ":" + str(server_port))
s.connect(('0.0.0.0',5005))

while True:
    client_address = ('0.0.0.0.')
    status = 'ok'
    print("Echoing back"+ str(status) + " to " + str(client_address))
    sen = s.sendto(status.encode(),clientaddress)