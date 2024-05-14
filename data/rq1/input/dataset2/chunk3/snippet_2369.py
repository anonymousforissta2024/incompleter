#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from pydealer import Deck
from player import Player
from dealer import Dealer

class Table:

    shoe = None
    dealer = None
    player = None

    def __init__(self):
        self.shoe = Deck()
        self.shoe.rebuild = True
        self.shoe.shuffle()
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.player.bet()
        self.dealer.deal(self.shoe.deal(2))
        self.player.deal(self.shoe.deal(2))