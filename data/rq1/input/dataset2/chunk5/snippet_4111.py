#Source: https://stackoverflow.com/questions/56776920/having-trouble-typeerror-string-indeces-must-be-an-integer
numberString = 0
holder = 0
partOne = 0
partTwo = 0
counter = 0
num = 0

def isPalindrome(number):

    if number % 2 == 0: #EVEN
        numberString = str(number)
        holder = len(numberString)
        holder = holder // 2
        holder = int(holder)
        partTwo = numberString[-(holder),-1]
        partOne = numberString[0,(holder - 1)]
        if partOne == partTwo:
            return True
        else:
            return False

    elif number % 2 != 0:  #ODD
        numberString = str(number)
        holder = len(numberString) // 2
        partTwo = numberString[-(holder),-1]
        partOne = numberString[0, (holder - 1)]
        if partOne == PartTwo:
            return True 
        else:
            return False

for first in range(100,1000):
    for second in range(100,1000):
        num = first * second
        if isPalindrome(num) == True:
            print(num,'is a palindrome.')