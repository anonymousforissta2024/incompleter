#Source: https://stackoverflow.com/questions/47618186/python-class-init-override-typeerror-init-takes-5-positional-argumen
class Dog(Animal):
    __owner = ""

    def __init(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

dog = Dog('Max', 120, 50, 'Woff', 'Tom') #<==== HERE ERROR OCCURES