#Source: https://stackoverflow.com/questions/64063104/typeerror-d-format-a-number-is-required-not-str-getting-this-error-while-cre
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[-#-]  Listening on %s:%d" % (bind_port, bind_ip))

# this is our clint-hanadaling thread


def handle_client(client_socket):
    # print out what client sends
    request = client_socket.recv(1024)
    print("[* ] Received %s " % request)
    # send back a request
    client_socket.send("ACK!")
    client_socket.close()
    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))
        # spin up our client thread  to handle incoming data
        clinet_handler = threading.Thread(target=handle_client, args=client)
        clinet_handler.start()