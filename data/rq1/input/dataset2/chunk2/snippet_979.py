#Source: https://stackoverflow.com/questions/50145204/im-getting-this-error-typeerror-string-indices-must-be-integers
import time
import sys

class Player:

    def __init__(self):
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.maxhp = 20
        self.hp = self.maxhp
        self.attack = 1
        self.weapon = ""
        self.armor = ""
        self.weaponsOwned = {}
        self.armorsOwned = {}

    def checkHp(self):
        self.hp = max(0, min(self.hp, self.maxhp))

    def deadCheck(self):
        if self.hp == 0:
            print("You died!")
            sys.exit()

    def equipArmor(self):
        for armor in self.armorsOwned:
            select = 1
            if self.armor == armor:
                print(str(select) + ". " + str(armor["Name"]) + " (Equipped)")
            else:
                print(str(select) + ". " + str(armor["Name"]))
            select += 1
        armor_choice = input("Type the name of the armor you would like to equip\n")
        for i in self.armorsOwned:
            if armor_choice == i["Name"]:
                if self.armor == i:
                    print("You already have that equipped")
                else:
                    self.armor = i["Name"]
                    print("You equipped the {}".format(i["Name"]))
                    self.maxhp += i["Effect"]

class Enemy:

    def __init__(self, attack, maxhp, exp, gold):
        self.exp = exp
        self.gold = gold
        self.maxhp = maxhp
        self.hp = maxhp
        self.attack = attack

    def checkHp(self):
        self.hp = max(0, min(self.hp, self.maxhp))

    def enemyDeadCheck(self):
        if self.hp == 0:
            return True

class Shop:

    armors = {"BronzeArmor":{"Name": "Bronze armor",
                             "Cost": 30,
                             "Effect": 10},
              "SilverArmor":{"Name": "Silver armor",
                             "Cost": 75,
                             "Effect": 20}}

character = Player()
character.armorsOwned.update(Shop.armors["BronzeArmor"])
character.equipArmor()