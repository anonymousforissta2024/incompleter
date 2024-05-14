from itertools import product

def test(dictt):
    result = [dict(zip(dictt, sub)) for sub in product(*dictt.values())]
    return result
print('\nOriginal dictionary:')
print(students)
print('\nA key-value list pairings of the said dictionary:')
print(test(students))