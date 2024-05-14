#Source: https://stackoverflow.com/questions/57357818/how-can-i-fix-the-typeerror-of-my-dataclass-in-python
from dataclasses import dataclass

@dataclass
class Employee(object):
    name: str
    lastname: str
    age: int or None
    salary: int
    department: str

    def __new__(cls, name, lastname, age, salary, department):
        return object.__new__(cls)

    def __post_init__(self):
        if type(self.age) == str:
            self.age = int(self.age) or None

    def __str__(self):
        return f'{self.name}, {self.lastname}, {self.age}' 

dic = {"name":"abdülmutallip", 
"lastname":"uzunkavakağacıaltındauzanıroğlu", 
"age":"24", "salary":2000, "department":"İK", 
"city":"istanbul", "country":"tr", "adres":"yok", "phone":"0033333"}

a = Employee(**dic)
print(a)