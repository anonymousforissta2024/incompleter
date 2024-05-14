#Source: https://stackoverflow.com/questions/20014392/name-error-python-a-text-adventure-game
from items import *

class weapons(Item):
    def __init__(self, name, attack_damage, lifesteal = 0):
        super(weapons,self).__init__(name, value, quantity=1)
        self.attack_damage = attack_damage
        self.lifesteal = lifesteal