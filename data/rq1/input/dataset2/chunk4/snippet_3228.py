#Source: https://stackoverflow.com/questions/75403903/why-am-i-receiving-the-typeerror-str-object-cannot-be-interpreted-as-an-inte
def listen():
    host = input("Please enter your target host IP: ")
    port = input("Please enter target port: ")
    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))
    s.listen(5)
    conn, addr = s.accept()
    print("pwned: "+addr[0]+":"+str(addr[1]))


listen()