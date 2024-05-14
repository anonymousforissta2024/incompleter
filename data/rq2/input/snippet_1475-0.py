import socket
try:
    socket.inet_aton(addr)
    print('Valid IP')
except socket.error:
    print('Invalid IP')