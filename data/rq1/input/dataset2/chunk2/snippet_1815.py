#Source: https://stackoverflow.com/questions/21964297/typeerror-unorderable-types-function-int
#While loop function for user input
def numInput():
    numbers = []

    while True:
        num = int(input('Enter a number (-9999 to end):'))
        if num == -9999:
            break
        numbers.append(num)
    return numbers

#Average of all numbers function
def allNumAvg(numList):
    return sum(numList) / len(numList)


#Average of all positive numbers function
def posNumAvg(numList):
    for num in [numList]:
        if num > 0:
            posNum = sum(num)
            posLen = len(num)
    return posNum / posLen

#Avg of all negative numbers function
def nonPosAvg(numList):
    for num in [numList]:
        if num < 0:
            negNum = sum(num)
            negLen = len(num)
    return negNum / negLen

#Creates Dictionary
myDict = {'AvgPositive':posNumAvg(numInput), 'AvgNonPos':nonPosAvg(numInput), 'AvgAllNum':allNumAvg(numInput)}   

#Prints List
print ('The list of of all numbers entered is\n', numInput(),'\n')

#Prints Dictionary
print ('The dictionary with averages is\n', myDict)