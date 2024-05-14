#Source: https://stackoverflow.com/questions/62463683/instances-as-attributes-trying-to-make-a-class-an-attribute-error
class Battery():
    """Model batter for a electric car"""
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        """print statement about battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
class ElectricCar(Car):
    """Represent a electric car"""
    def __init___(self,make,model,year):
        """
        Initialize attributes of the parent class,
        then initialize attributes specific to electric car
        """
        super().__init__(make,model,year)
        self.battery = Battery()

new_tesla = ElectricCar('Big tesla',"model Z",'2020')
new_tesla.battery.describe_battery()