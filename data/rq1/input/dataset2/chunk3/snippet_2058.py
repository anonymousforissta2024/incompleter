#Source: https://stackoverflow.com/questions/56009331/how-do-i-fix-this-typeerror-in-python
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