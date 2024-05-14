#Source: https://stackoverflow.com/questions/45315616/python-typeerror-object-takes-no-parameters-error
class showInfo(object):
    'Initialize a classL'
    def __int__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age

def showName(self):
    print("Name: "+self.name)
def showAge(self):
    print("Age: "+self.age)
def showPhone(self):
    print("Phone: "+self.phone)

emp1 = showInfo("JJJ")

emp1.showName()