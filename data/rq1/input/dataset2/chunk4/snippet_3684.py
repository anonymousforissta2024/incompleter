#Source: https://stackoverflow.com/questions/62234344/why-does-my-code-say-nameerror-name-self-is-not-defined
import random
def getName():
    syllables = ['en','da','fu','ka','re','toh','ko','noh','tuk','el','kar']
    firstName = (random.choice(syllables))
    secondName = (random.choice(syllables))
    thirdName = (random.choice(syllables))
    global generatedName
    generatedName = firstName+'-'+secondName+'-'+thirdName



# Classes-all creatures have names generated the same way and have the same amount of health.
# The way I have selected how each subclass will be randomly chosen is having the code select a random value
# from the list and depending on which is chosen it will give a subclass.
class preset():
    def _init_(self, creature, name, health=100):
        self.name = generatedName
        self.health = 100
        getName()
        self.name=generatedName


#Gives different attributes to each sub-class        
class barbarian(preset):
    def _init_(self, name, power=70, specialAttackPower=20, speed=50):
        preset._init_(self, creature, name, health=100)
        self.power = power
        self.specialAttackPower = specialAttackPower
        self.speed = speed
        self.name = name

    def returnBarbarianStats():
        print(self.name,"the barbarian's stats:")
        print("Health:",self.health)
        print("Power damage:",self.power)
        print("Special attack power damage:",self.specialAttackPower)
        print("Speed:",self.speed)

class elf(preset):
    def _init_(self, name, power=30, specialAttackPower=60, speed=10):
        preset._init_(self, creature, name, health=100)
        self.power = power
        self.specialAttackPower = specialAttackPower
        self.speed = speed

class wizard(preset):
    def _init_(self, name, power=50, specialAttackPower=70, speed=30):
        preset._init_(self, creature, name, health=100)
        self.power = power
        self.specialAttackPower = specialAttackPower
        self.speed = speed

class dragon(preset):
    def _init_(self, name, power=90, specialAttackPower=40, speed=50):
        preset._init_(self, creature, name, health=100)
        self.power = power
        self.specialAttackPower = specialAttackPower
        self.speed = speed

class knight(preset):
    def _init_(self, name, power=60, specialAttackPower=10, speed=60):
        preset._init_(self, creature, name, health=100)
        self.power = power
        self.specialAttackPower = specialAttackPower
        self.speed = speed

#10 randomly generated characters.
i = 0
army = []
while i < 10:
    creatures = ['barbarian','elf','wizard','dragon','knight']
    creatureType = (random.choice(creatures))
    if creatureType == 'barbarian':
        army.append(barbarian())
    elif creatureType == 'elf':
        army.append(elf())
    elif creatureType == 'wizard':
        army.append(wizard())
    elif creatureType == 'dragon':
        army.append(dragon())
    elif creatureType == 'knight':
        army.append(knight())
    i = i + 1

barbarian.returnBarbarianStats()