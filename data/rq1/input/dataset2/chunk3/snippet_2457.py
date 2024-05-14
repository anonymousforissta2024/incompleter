#Source: https://stackoverflow.com/questions/57298549/how-do-i-debug-this-attributeerror-int-object-has-no-attribute-increase
class Employee:
    """Sort of simulates an employee."""

    def __init__(self, first, last, salary):
        """Initialize attributes."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, increase = 5000):
        """gives raise"""
        self.increase = increase
        self.salary = self.salary + self.increase

Employee("first", "last", 30000)
Employee.give_raise(890)
print(Employee.salary)