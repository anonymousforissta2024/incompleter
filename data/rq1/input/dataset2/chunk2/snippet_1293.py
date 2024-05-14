#Source: https://stackoverflow.com/questions/45250605/typeerror-object-takes-no-parameters-when-creating-an-object
class Human:
    __name = None
    __height = 0

def __init__(self, name, height):
    self.__name = name
    self.__height = height

def set_name(self, name):
    self.__name = name

def get_name(self):
    return self.__name

def set_height(self, height):
    self.__height = height

def get_height(self):
    return self.__height

def get_type(self):
    print('Human')

def toString(self):
    return '{} is {} cm tall.'.format(self.__name,
                                      self.__height)

person = Human('Corey', 180)