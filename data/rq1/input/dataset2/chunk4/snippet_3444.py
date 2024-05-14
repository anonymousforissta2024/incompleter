#Source: https://stackoverflow.com/questions/37363764/python3-abstract-class-typeerror-not-raised
from abc import ABCMeta, abstractmethod

class Base(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    pass


confused = Concrete()