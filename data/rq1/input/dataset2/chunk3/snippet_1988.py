#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from hand.py import Hand

class Player:

    hands = []
    __chips = None
    __betamount = None

    def __init__(self):
        self.__chips = 5000

    def bet(self):
        type(self.__betamount)

    def __deal(self, twocards):
        self.hands = [Hand(showfirst=True)]
        self.hands[0] += twocards
        self.hands[0].showcards()

    def hit(self, card, whichhand):
        self.hands[whichhand] += card

    def stay(self, whichhand):
        self.hands[whichhand].setstay()

    def printscore(self, whichhand):
        print(self.hands[whichhand].stackscore())