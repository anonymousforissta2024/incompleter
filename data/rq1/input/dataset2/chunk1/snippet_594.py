#Source: https://stackoverflow.com/questions/30174847/typeerror-attack-missing-1-required-positional-argument-self
class Enemmy :
    life = 3
    self = ""
    def attack(self):
        print ("ouch!!!!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0 :
            print ("dead")
        else:
            print (self.life)

enemy=Enemmy
enemy.attack()