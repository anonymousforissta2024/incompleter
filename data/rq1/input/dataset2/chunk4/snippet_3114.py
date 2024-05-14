#Source: https://stackoverflow.com/questions/67847906/typeerror-when-dividing-two-integers-and-printing
num1=input("Enter a number: ")
num2=input("Enter the divisor: ")
result = 0
def findRemainder(x, y):
    result = (x%y)
    print(str(result))
findRemainder(num1, num2)