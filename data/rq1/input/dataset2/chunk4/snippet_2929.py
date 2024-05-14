#Source: https://stackoverflow.com/questions/68953459/attributeerror-str-object-has-no-attribute-describe
class Computer:

    def _inti_(self, storage, color , system):
        no_of_Computer = 0
        self.storage = storage
        self.color = color
        self.system = system
        Computer.no_of_Computer +=1

    def describe (self):

        print(f'my storage is {self.storage} and my color is{self.color} and my system is {self.system}')

Computer_1 = ("1TB ,  silver , windows ")

Computer_2 = (" 4TB , black , linux")

Computer_3 = (" 9TB , white ,mac ")

Computer_1.describe()