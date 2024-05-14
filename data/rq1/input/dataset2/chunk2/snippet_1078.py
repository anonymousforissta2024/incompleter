#Source: https://stackoverflow.com/questions/75543849/python-typeerror-init-takes-1-positional-argument-but-4-were-given-pro
class Student:
    def __init__(self, name,age,subject):
        self.name = name
        self.age = age
        self.subject = subject

    def subjchoosen(self):
        print("The subject choosen is",self.subject )

class Science(Student):
    def __init__(self):
        super().__init__(name, age,subject)
        super().subjchoosen()

name = "Test"
age = 12
subject = "Science"
Sc=Science(name,age,subject)