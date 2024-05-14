#Source: https://stackoverflow.com/questions/28272322/typeerror-slice-indices-must-be-integers-or-none-or-have-an-index-method
from collections import deque

m = []
f = open("IntegerArray.txt")
for line in f:
    m.append(int(line))

class InversionCount:

    def __init__(self, n):
        self.n = n
    def inversionMergeSort(self, m):
        if len(m) <= 1:
            return m
        half = len(m)/2
        left = m[0:half]
        right = m[half:]
        left = self.inversionMergeSort(left)
        right = self.inversionMergeSort(right)
        return self.inversionSort(left, right)

    def inversionSort(self, left, right):
        leftQueue = deque(i for i in left)
        rightQueue = deque(j for j in right)
        orderedList = []
        while len(leftQueue) > 0 or len(rightQueue) > 0:
            if len(leftQueue) > 0 and len(rightQueue) > 0:
                if leftQueue[0] <= rightQueue[0]:
                    orderedList.append(leftQueue[0])
                    leftQueue.popleft()
                else:
                    orderedList.append(rightQueue[0])
                    self.n += len(leftQueue)
                    rightQueue.popleft()
            elif len(leftQueue) > 0:
                orderedList.append(leftQueue[0])
                leftQueue.popleft()
            elif len(rightQueue) > 0:
                orderedList.append(rightQueue[0])
                rightQueue.popleft()
        return orderedList

nInversions = InversionCount(0)
nInversions.inversionMergeSort(m)
print (nInversions.n)