#Source: https://stackoverflow.com/questions/76940145/using-multiple-inheritance-getting-typeerror-init-missing-1-required-po
class Employee:
    def __init__(self, id, ename):
        self.id = id
        self.ename = ename

    def showInfo(self):
        print("ID=", self.id, "Name of employee=", self.ename)

class Programmer(Employee):
    def __init__(self, id, ename, language):
        super().__init__(id, ename)
        self.language = language

    def showInfo(self):
        super().showInfo()
        print("Development Language=", self.language)

class Manager(Employee):
    def __init__(self, id, ename, department):
        super().__init__(id, ename)
        self.department = department

    def showInfo(self):
        super().showInfo()
        print("Department=", self.department)

# Define Development Manager class using Multiple inheritances
class DevManager(Programmer, Manager):
    def __init__(self, id, ename, language, department):
        Programmer.__init__(self, id, ename, language)
        Manager.__init__(self, id, ename, department)

    def showInfo(self):
        super().showInfo()

# Main
obj = DevManager("A101", "Rajib Menon", "Python", "Engineering")
obj.showInfo()