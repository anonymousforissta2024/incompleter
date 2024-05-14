#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from CustomExceptions import InvalidPlayerNumException

class Player:
    # custom constructor. Constructors are named __init__()
    def __init__(self, name, number):
        # set the attributes
        # note the single underscore _ before the variable name makes them protected
        self._name = name
        self.set_number(number) # note we call the setter method here


    # getter and setter methods for the various properties
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number

    def set_number(self, number):
        MIN_NUMBER = 1
        MAX_NUMBER = 999

        # Add validation to make sure number is in the expected range
        if number >= MIN_NUMBER and number <= MAX_NUMBER:
            self._number = number
        else:
            # instead of setting player number to MIN_NUMBER, raise an exception
            #self._number = MIN_NUMBER # original code
            raise InvalidPlayerNumException


    # instance method
    def to_string(self):
        return "Name: " + self._name + " Number: " + str(self._number)