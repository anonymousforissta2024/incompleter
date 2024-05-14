#Source: https://stackoverflow.com/questions/9539156/typeerror-in-python-3-x
class Student:
    '''Student class'''

    name = None
    id = 0
    address = None
    cgpa = None

    def get_name():
        return name

    def set_name(n):
        name = n

    def get_id():
        return id

    def set_id(i):
        id = i

    def get_address():
        return address

    def set_address(a):
        address = a

    def get_cgpa():
        return cgpa

    def set_cgpa(c):
        cgpa = c


#An object of Student class
jack = Student()

jack.set_name('jacky')
print(jack.get_name())