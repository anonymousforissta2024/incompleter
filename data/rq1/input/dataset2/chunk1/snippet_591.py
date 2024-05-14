#Source: https://stackoverflow.com/questions/59118509/defining-property-setter-in-abstract-base-class-gives-attributeerror
from abc import ABC, abstractmethod

def reload_data():
    return ['hello']


class Base(ABC):
    @property
    @abstractmethod
    def data(self):
        pass

    @data.setter               # <----- AttributeError if this is defined here
    def data(self, value):
        self._data = value


class Foo(Base):
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = reload_data()
        return self._data

    # @data.setter              # <----- Defining it here avoids AttributeError, but 
    # def data(self, value):             causes code repetition in all the subclasses of Base
    #     self._data = value

foo = Foo()
foo.data = ['world']
print(foo.data)