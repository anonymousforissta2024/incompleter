#Source: https://stackoverflow.com/questions/62626731/typeerror-car-takes-no-arguments
class Car:
   def __rep__(self):
        return f'Car({self.name},{self.year_built},{self.model})'


c1 = Car('minicooper','1970','MX1')