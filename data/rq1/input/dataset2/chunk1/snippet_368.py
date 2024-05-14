#Source: https://stackoverflow.com/questions/41606555/typeerror-object-takes-no-parameters
class Person(object):
    def __new__(cls, name, age):
        print('__new__called')
        return super(Person, cls).__new__(cls, name, age)
    def __init__(self, name, age):
        print('__init__called')
        self.name = name
        self.age = age
    def __str__(self):
        return('<Person:%s(%s)>'%(self.name, self.age))
if __name__ == '__main__':  
    piglei = Person("piglei", 24)
    print(piglei)