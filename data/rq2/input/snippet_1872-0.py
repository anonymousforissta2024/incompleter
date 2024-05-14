def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))