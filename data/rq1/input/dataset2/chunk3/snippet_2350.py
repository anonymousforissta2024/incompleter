#Source: https://stackoverflow.com/questions/61651817/i-am-getting-type-error-in-multiple-inheritance-in-python-opp
import  random


class Coin:
    def flip(self):
        #toss=int(input('how many times you want to tosses the coin?: '))
        for i in range(self):
            rand=random.randint(-1,1)
            if rand==1:
                return rand
                #print("head")
            else:
                return rand
                #print('tail')
    print(flip(4))

class Dice:
    def roll(self):
        #x=int(input("inter number"))
        for x in range(self):
            points=random.randint(1,6)
            return points
    print(roll(5))

class Player(Coin,Dice):
    def rolls(self):
        # x=int(input("inter number"))
        for x in range(self):
            points = random.randint(1, 6)
            return points

    print(rolls(5))


obj=Player()
obj.flip()
obj.roll()