#Source: https://stackoverflow.com/questions/26985054/python-3-type-error-object-new-takes-no-parameters
#create the car class
class Car:

    #create the initiator function
    def __init__carStats(self, year, model):
        self.__speed = 0
        self.__year = year
        self.__model = model

    def setModel(self, model):
        self.__model = model

    def setYear(self, year):
        self.__year = year

    #create speed increase function
    def speedUp(self):
        print('Calling speed up function.')
        self.__speed += 5

    #create slowdown function
    def slowDown(self):
        print('Calling slow down function.')
        self.__speed -= 5

    #create show speed function
    def showSpeed(self):
        print('The', self.__year, self.__model, '\'s current speed is', self.__speed,'miles per houer')

#create main function
def Main():
    year = ''
    make = ''
    #get car year and make
    make = input('What model is the car? \n')
    year = input('What year is the car?" \n')

    myCar = Car(year, make)

Main()