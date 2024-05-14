#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
import pydealer

class Hand(pydealer.Stack):

    stay = None
    showfirstcard = None
    bust = None

    def __init__(self, showfirst, **kwargs):
        super().__init__(**kwargs)
        stay = False
        self.showfirstcard = showfirst

    def stackscore(self):
        total = 0
        for card in self:
            total += self.__bjval(card)
        if total > 21:
            for card in self:
                if card.value == "Ace":
                    total -= 10
                if total <= 21:
                    break
        return total

    def __bjval(self, card):
        return {
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'Jack': 10,
                'Queen': 10,
                'King': 10,
                'Ace':11
                }[card.value]

    #def receive(self, cards):
        #self += cards

    def setstay(self):
        self.stay = True

    def getsize(self):
        return self.size()

    def showcards(self):
        for i, card in enumerate(self):
            if i == 0:
                if self.showfirstcard == False:
                    print('***FACEDOWN CARD***')
                else:
                    print(card)