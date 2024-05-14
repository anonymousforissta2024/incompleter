#Source: https://stackoverflow.com/questions/45269822/getting-error-in-python-3-x-typeerror-int-object-is-not-callable
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        car_name = str(self.year) + ' ' + self.make + ' ' + self.model + 'model.'
        return car_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_dream_car = Car('lamborghini', 'one-off', 2017 )
print("\nMy dream car is " + my_dream_car.get_descriptive_name())
my_dream_car.odometer_reading = 23
my_dream_car.odometer_reading()