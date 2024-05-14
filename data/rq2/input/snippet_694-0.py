from collections import Counter

def test(dictt):
    result = Counter(dictt.values())
    return result
print('\nOriginal Dictionary:')
print(dictt)
print('\nCount the frequency of the said dictionary:')
print(test(dictt))