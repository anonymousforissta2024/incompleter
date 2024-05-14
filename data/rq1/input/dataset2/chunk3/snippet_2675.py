#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
class Hand(pydealer.Stack):

    def __init__(self, showfirst, **kwargs):
        super().__init__(**kwargs)
        stay = False
        self.showfirstcard = showfirst

    ...

    def showcards(self):
        for i, card in enumerate(self):
            if i == 0:
                if self.showfirstcard == False:
                    print('***FACEDOWN CARD***')
                else:
                    print(card)