#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from CustomExceptions import InvalidAge

class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self.set_age(age)

        # getter and setter methods for the various properties
        def get_name(self):
            return self._name

        def set_name(self, name):
            self._name = name

        def get_address(self):
            return self._address

        def set_address(self, address):
            self._address = address

        def get_age(self):
            return self._age

        def set_age(self, age):
            MIN_AGE = 0
            MAX_AGE = 120

            if age >= MIN_AGE and age <= MAX_AGE:
                self._age = age
            else:
                raise InvalidAge

    # instance method
    def to_string(self):
        return "Name: " + self._name + " Address: " + self._address + " Age: " + str(self._age)