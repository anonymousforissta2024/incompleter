#Source: https://stackoverflow.com/questions/54071217/attributeerror-module-socket-has-no-attribute-msg-dontwait
RECV_BUFFER_SIZE = 1024
buff = memoryview(bytearray(RECV_BUFFER_SIZE))
x = client_socket.recv_into(buff, RECV_BUFFER_SIZE, socket.MSG_DONTWAIT)