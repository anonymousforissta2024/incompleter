#Source: https://stackoverflow.com/questions/57908392/typeerror-init-takes-4-positional-arguments-but-5-were-given-added-all-e
class Employee:
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email="{}{}@company.com".format(first,last)


class administrator:
    def __init__(self,age):
        self.age=age

class Manager(Employee,administrator):
    def __init__(self,first,last,salary,age,gender):

        super().__init__(first,last,salary,age)
        self.gender=gender

manager1=Manager("Max","Milan",50000,26,"male")

print(manager1.email)
print(manager1.gender)