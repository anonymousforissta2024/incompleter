#Source: https://stackoverflow.com/questions/77680000/typeerror-sslcontext-wrap-socket-missing-1-required-positional-argument-soc
import ssl 
import socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ssl_sock = ssl.SSLContext.wrap_socket(sock)