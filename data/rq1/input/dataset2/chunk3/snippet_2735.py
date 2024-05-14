#Source: https://stackoverflow.com/questions/43903884/attributeerror-when-assigning-to-a-manager-dict-in-a-child-process
import multiprocessing
from socketserver import UDPServer, ForkingMixIn, DatagramRequestHandler
from socket import socket, AF_INET, SOCK_DGRAM
from settings import host, port, number_of_connections

class ChatHandler(DatagramRequestHandler):

    def handle(self):
        cur_process = multiprocessing.current_process()
        data = self.request[0].strip()
        socket = self.request[1]
        ChatHandler.clients.append(self.client_address) # error here
        print(ChatHandler.clients)


class ChatServer(ForkingMixIn, UDPServer):
    pass


if __name__ == '__main__':
    server = ChatServer((host, port), ChatHandler)
    ChatHandler.clients = multiprocessing.Manager().list()
    server_process = multiprocessing.Process(target=server.serve_forever)
    server_process.daemon = False
    server_process.start()