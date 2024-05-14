#Source: https://stackoverflow.com/questions/20023345/another-name-error-for-my-text-adventure-game-python
class character(object):
    def __init__(self,name,hp,maxhp):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
    def attack(self,other):
        pass



p=player(Players_name, 100, 100, 10, 5,)
while (p.hp>0):
    a=input("What do you want to do?")
    if a=="Instructions":
        Instructions()
    elif a=="Commands":
        Commands()
    elif a=="Fight":
        print("Level",wave,"Wave Begins")
        if wave < 6:
            b = random_enemies.weak()
            print("A",b,"Appeared!")
            print("Stats of",b, ": \n Health=", b.hp,"Attack Damage=",b.attack_damage)
            continue