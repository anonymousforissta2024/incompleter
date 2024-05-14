#Source: https://stackoverflow.com/questions/51636107/why-does-the-below-code-throw-typeerror
class Car:
    def __init__(self, mileage, make, model):
        self.mileage = mileage
        self.make = make
        self.model = model

    def printCar(self):
        return "The Model is:" + self.model + " the make is: " + self.make + " and the mileage is: " + self.mileage


car = Car(100, 'Suzuki', 'Brezza')

print(car.printCar())