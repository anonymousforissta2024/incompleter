#Source: https://stackoverflow.com/questions/40110816/attributeerror-nonetype-object-has-no-attribute-recv
from src.lib import irc as irc_

from src.lib import functions_general

from src.lib import functions_commands as commands

from src.config import config

class PartyMachine:

    def __init__(self, config):
        self.config = config
        self.irc = irc_.irc(config)
        self.socket = self.irc.get_irc_socket_object()


    def sock(self):
        irc = self.irc
        sock = self.socket
        config = self.config
        kage = sock

        while True:
            data = sock.recv(2048).rstrip()

            if len(data) == 0:
                pp('Connection was lost, reconnecting.')
                sock = self.irc.get_irc_socket_object()

            if config['debug']:
                print (data)