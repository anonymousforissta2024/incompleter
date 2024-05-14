#Source: https://stackoverflow.com/questions/66610777/typeerror-module-object-is-not-callable-call-to-constructor
from com.gs.entities import Employee
from _datetime import datetime, timedelta


class Branch:

    def __init__(self, branchName):
        self.branchName = branchName
        self.startTime = datetime.now()
        self.endTime = datetime.now() + timedelta(hours = 9)
        self.employees = []
        for i in range(0, 10):
            if(i < 6):
                self.employees.append(Employee(i, str(i), "Cashier"))
            elif(i < 8):
                self.employees.append(Employee(i, str(i), "Loan Officers"))
            elif(i == 8):
                self.employees.append(Employee(i, str(i), "Deputy Manager"))
            elif(i == 9):
                self.employees.append(Employee(i, str(i), "Manager"))
        
    def startOperation(self):
        print("Starting operation at " + self.startTime)

    def endOperation(self):
        print("Starting operation at " + self.endTime)


b = Branch("CP")
print(b.employees)