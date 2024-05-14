#Source: https://stackoverflow.com/questions/46781937/missing-arguments-and-type-errors
def bs(L, item, left, right):
    if right is None:
        right = len(L)
    if right - left == 0:
        return False
    if right - left == 1:
        return L[left] == item
    median = (right + left)//2
    if item < L[median]:
        return bs(L, item, left, median)
    else:
        return bs(L, item, median, right)

L = [i for i in range(10)]
for i in range(20):
    print(bs(L, i))