#Source: https://stackoverflow.com/questions/52434994/python-getting-attributeerror-electriccar-object-has-no-attribute-battery
class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + str(self.make) + ' ' +str(self.model)
        return long_name.title()
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('you cant roll it back')


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        " ""Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

#The call to the battery attribute in the ElectricCar class is where the         
#error emanates
class ElectricCar(Car):
    def __inti__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_telsa = ElectricCar('Volvo', 'models s', 2006)
print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()