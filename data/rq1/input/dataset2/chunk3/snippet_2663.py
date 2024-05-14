#Source: https://stackoverflow.com/questions/51315053/nameerror-while-trying-to-extend-a-class
from Charmander import *
from Bulbasaur import *
from Turtwig import *
class Pokemon:
    def __init__(self, current_hp, attack, defense):
        self.name = "PlaceHolder"
        self.pokemon_type = "PlaceHolder"
        self.current_hp = current_hp
        self.attack = attack
        self.defense = defense
        self.fainted = False

    def getName(self):
        return self.name

    def getType(self):
        return self.pokemon_type

    def getCurrentHP(self):
        return self.current_hp

    def getHealth(self):
        return self.current_hp

    def getAttack(self):
        return self.attack

    def getDefense(self):
        return self.defense

    def getFainted(self):
        return self.fainted

    def printStatus(self):
        print(self.name)
        print(str(self.current_hp))
    def takedamage(self, amount):
        self.current_hp -= amount
    def tackle(self, opponent):
        opponent.current_hp -= self.attack

    def die(self, opponent):
        self.fainted = True
        if self.current_hp == 0:
            print("You Lose!")
        elif(opponent.current_hp == 0):
            print("You win!")

    def checkDead(self, opponent):
        if self.current_hp == 0 or opponent.current_hp == 0:
            self.die(opponent)

    def assignPokemon(self, player):
        if player == "Charmander":
            player = Charmander(200, 20, 20)
        if player == "Bulbasaur":
            player = Bulbasaur(200, 20, 20)
        if player == "Turtwig":
            player = Turtwig(200, 20, 20)
        return player