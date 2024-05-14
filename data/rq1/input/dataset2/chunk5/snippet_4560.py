#Source: https://stackoverflow.com/questions/43697088/typeerror-removeduplicates-missing-1-required-positional-argument-randlist
from random import randrange

def createList():
    print("A program that will generate a list of 50 random numbers then remove any duplicates.")
    for i in range(50):
        randList = randrange(101)
        print(randList)

def removeDuplicates(randList):
    uniqueList = []
    for i in randList:
        if i not in uniqueList:
            uniqueList.append(i)
    print(uniqueList)

def main():
    createList()
    removeDuplicates()

if __name__ == "__main__": main()