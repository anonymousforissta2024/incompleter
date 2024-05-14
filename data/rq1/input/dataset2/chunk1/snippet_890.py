#Source: https://stackoverflow.com/questions/54308619/how-to-fix-a-type-error-for-non-iterabble-socket-object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# just a list of connections
connection = {

}
def n_remover(user):
    with open("UserPass.txt" , 'r') as f:
        passuser = f.readlines()
        for x in passuser:
            print(x)
            for area, value in enumerate(x):
                print(value, area)
                if value == '\n':
                    print(value,area)
                    passuser[passuser.index(x)] = passuser[passuser.index(x)][0:area]
                    print(passuser[0])
        return passuser[passuser.index(user)]

def file_len(file):
    with open('UserPass.txt', 'r') as f:
        for length, value in enumerate(f):
            pass
    return length+1

# this bind the server to any ip in ipv4 and any port above 10000
def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

# this handles sending out data to all of the users and handels the disconnect of a user the a arg is a ip and port. and c is the threaded connection.
def handler(self, c, a):
    while True:
        data = c.recv(1024)
        print(str(data)[0:1])
        if str(data)[0:1] == "/p":
            datasplit = (str(self.data)).split(" ")
            password_name = [self.datasplit[1] + ' ' + self.datasplit[2]]
            with open("UserPass.txt" , 'r+') as f:
                passuser = n_remover(password_name)
                for key, value in connection:
                    if c == key:
                        self.connection[c] = self.datasplit[1]
        else:
            print(self.connection)

            try:
                l = self.connection[c]

            except IndexError:
                self.connection[c] = "anon"

            for key,value in self.connection:
                key.send(bytes(self.connection[c] + ': ' + data))

            if not data:
                print(str(a[0]) + ':' + str(a[1], "disconnected"))
                del self.connection[c]
                c.close
                break