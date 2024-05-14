#Source: https://stackoverflow.com/questions/75403903/why-am-i-receiving-the-typeerror-str-object-cannot-be-interpreted-as-an-inte
# create the if loop for option 2, port listener.
if choice=='2':
# take the target host ip as user input and store it in a variable
    host = input('Please enter target host: ')
# take the target port and store it in a variable
    port = int(input('Please enter target port'))
# check the connection for errors
    try:
        s.bind((host, port))
# if the connection fails, display an error message.
    except socket.error as e:
        print(str(e))
# listen for the connection with the maximum number of queued connections being five.
    s.listen(5)
# accept the connection from client
    conn, addr = s.accept()
# display a message on the client machine.
    print('pwned: '+addr[0]+':'+str(addr[1]))