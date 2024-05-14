#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from player import Player
from hand import Hand

class Dealer(Player):

    def __init__(self):
        super().__init__()

    def deal(self, twocards):
        self.hands = [Hand(showfirst=False)]
        self.hands[0] += twocards
        self.seecards(0)