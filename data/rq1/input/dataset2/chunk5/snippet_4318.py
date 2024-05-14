#Source: https://stackoverflow.com/questions/20023345/another-name-error-for-my-text-adventure-game-python
import random
from character import *
from player import *

class random_enemies(character):
    def __init__(self,name,hp,maxhp,attack_damage,ability_power,exp):
        super(random_enemies,self).__init__(name,hp,maxhp)
        self.attack_damage = attack_damage
        self.ability_power = ability_power
        self.exp = exp
    def weak():
        self.hp = random.randint(p.maxhp/10, p.maxhp/5)
        self.attack_damage = None
        self.ability_power = None
        self.exp = None



from character import*
class player(character):
    def __init__(self,name,hp,maxhp,attack_damage,ability_power):
        super(player,self).__init__(name, hp, maxhp)
        self.attack_damage = attack_damage
        self.ability_power = ability_power