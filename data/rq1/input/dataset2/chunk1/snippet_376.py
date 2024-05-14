#Source: https://stackoverflow.com/questions/46505037/typeerror-cant-instantiate-abstract-class-with-abstract-methods
from abc import ABC
from abc import abstractmethod

class Mamifiero(ABC):
    """docstring for Mamifiero"""
    def __init__(self):
        self.alimentacion = 'carnivoro'
    
    @abstractmethod
    def __respirar(self):
        print('inhalar... exhalar')
    
class Perro(Mamifiero):
    """docstring for Perro"""
    def __init__(self, ojos=2,):
        self.ojos = ojos