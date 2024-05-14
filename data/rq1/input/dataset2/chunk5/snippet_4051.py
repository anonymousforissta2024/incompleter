#Source: https://stackoverflow.com/questions/56414033/python-nameerror-name-is-not-defined-in-bankaccount-example
class BankAccount:
    def __init__(self, FirstName, LastName, AccNum, Balance, CreationYear, CreationMonth, CreationDay):
        self.FirstName = FirstName
        self.LirstName = LirstName
        self.AccNum = AccNum
        self.Balance = Balance
        self.CreationYear = CreationYear
        self.CreationMonth = CreationMonth
        self.CreationDay = CreationDay

    def AddAccount(self):
        self.FirstName = input("First Name: ")
        self.LastName = input("Last Name: ")
        self.AccNum = input("Account Number: ")
        self.Balance = input("Balance: ")
        self.CreationYear = input("Creatin Year: ")
        self.CreationMonth = input("Creation Month: ")
        self.CreationDay = input("Creation Day: ")
        return self.FirstName , self.LastName , self.AccNum , self.Balance , self.CreationYear , self.CreationMonth , self. CreationDay


    def Deposit(self):
        amount = input("How much do you want to Deposit? ")
        self.Balance = str(float(amount) + float(self.Balance))
        print("Balance: ", self.Balance)
        return self.Balance

    def Withdrawl(self):
        amount = input("How much do you want to withdrawl? ")
        if (float(amount) > float(self.Balance)):
            print("Insufficent Balance.")
        else:
            self.Balance = str(float(self.Balance) - float(amount))
            print("Balance: ", self.Balance)
        return self.Balance


x = BankAccount(FirstName, LastName, AccNum, Balance, CreationYear, CreationMonth, CreationDay)
x.AddAccount()