#Source: https://stackoverflow.com/questions/64991199/attributeerror-on-python-with-an-encapsulation-object-hasn%c2%b4t-got-an-attribute
class Car():

    def __init__(self):

       self.__doors=4
       self.sizeChasis=250
       self.colorChasis=120
       self.running=False

    def start(self,letsgo):
        self.running=letsgo

        if(self.running):
            return "Car is on"
        else:
            return "Car is off"

    def state(self):
        print("The car has ", self.__doors, "doors. And ", self.sizeChasis, "and ", self.colorChasis)

myCar=Car()

print("A: ",myCar.sizeChasis)
print("B: ", myCar.__doors, "doors")

print(myCar.start(True))
myCar.state()