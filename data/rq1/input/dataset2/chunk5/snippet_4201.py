#Source: https://stackoverflow.com/questions/60381236/undefined-name-error-in-python-socket-module
from socket import socket
import sys 

serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)