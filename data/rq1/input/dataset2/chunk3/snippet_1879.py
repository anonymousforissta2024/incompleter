#Source: https://stackoverflow.com/questions/50835149/attributeerror-employee-object-has-no-attribute-workinghours
class Employee:
    def numberofWorkingHours(self):
        self.WorkingHours = 45

    def printnumberofWorkingHours(self):
        print(self.WorkingHours)

class Trainee:
 def numberofWorkingHours(self):
     self.WorkingHours = 60

emp = Employee()
emp.printnumberofWorkingHours()