#Source: https://stackoverflow.com/questions/75232827/python3-class-error-typeerror-employees-takes-no-arguments
from Employees import Employees

e1 = Employees("Bob", "Sales", "Director of Sales", 1000000, 20)
e2 = Employees("Linda", "Executive", "CIO", 150000, 35)

print(e1.name)
print(e2.role)