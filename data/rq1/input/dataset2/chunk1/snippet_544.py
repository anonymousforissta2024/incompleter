#Source: https://stackoverflow.com/questions/42612002/python-sockets-error-typeerror-a-bytes-like-object-is-required-not-str-with
s = socket.socket()
host = '127.0.0.1'
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()