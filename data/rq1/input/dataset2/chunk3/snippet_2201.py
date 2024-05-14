#Source: https://stackoverflow.com/questions/51315053/nameerror-while-trying-to-extend-a-class
from pokemon import *
class Charmander(Pokemon):
    pass
    def __init__(self, current_hp, attack, defense):
        self.name = "Charmander"
        self.type = "Fire"
        self.current_hp = 200
        self.attack = 10
        self.defense = 10

    def ember(self, opponent):
        opponent.takeDamage(40)

    def will_o_wisp(self, opponent):
        return

    def flamethrower(self, opponent):
        opponent.takeDamage(90)