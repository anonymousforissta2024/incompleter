#Source: https://stackoverflow.com/questions/39112489/typeerror-unsupported-operand-types-for-str-and-str
import math

class Cashier:

    def getDollars(self, x):
        return x / 100

    def getQuarters(self, x):
        y = x % 100
        return y / 25

    def getDimes(self, x):
        y = x % 100
        return y % 10

    def getNickels(self, x):
        y = x % 100
        return y % 5

    def getPennies(self, x):
        y = x * 1
        return y

while True:

    thecashier = Cashier()

    amountDue = input("Please enter amount due: ")
    amountReceived = input("Please enter amount received: ")

    changePennies = int((amountReceived - amountDue) * 100)

    print(thecashier.getPennies(changePennies))
    print(thecashier.getDollars(changePennies))
    print(thecashier.getQuarters(changePennies))
    print(thecashier.getDimes(changePennies))
    print(thecashier.getNickels(changePennies))

    choice = input("Do you want to continue <yes> <no>? ")
    if (choice == "no"):
        print("Have a nice day. ")
        break