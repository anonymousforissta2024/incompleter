#Source: https://stackoverflow.com/questions/27092337/why-am-i-getting-a-typeerror-unsupported-operand-types-for-nonetype-and-int
def testDenary(testValue):
    if testValue < int(0):
        print("Error: Negative value input. Please try again!")
        return False
    elif testValue > 255:
        print("Error: Input value too high. Please try again!")
        return False
    else:
        return True

def getDenary():
    denIn = int(input("Please enter a number between 0 and 255: "))
    if testDenary(denIn):
        return denIn
    else:
        getDenary()

def convertToBinary(denaryIn):
    x = 0
    result = []
    for number in range(8):
        bit = denaryIn % 2
        result.append(bit)
        denaryIn = denaryIn // 2
        print (type(denaryIn))
    result.reverse()
    str1 = "".join(str(x)for x in result)
    return str1

def main():
    denary = getDenary()
    answer = convertToBinary(denary)
    print ("Binary version = " + answer)
    main()

main()