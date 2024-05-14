#Source: https://stackoverflow.com/questions/20014392/name-error-python-a-text-adventure-game
from character import*
class player(character):
    def __init__(self,name,hp,maxhp,attack_damage,ability_power):
        super(player,self).__init__(name, hp, maxhp)
        self.attack_damage = attack_damage
        self.ability_power = ability_power