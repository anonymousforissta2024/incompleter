def test(dictt):
    min_value = 1
    result = [k for k, v in dictt.items() if len(v) == min_value]
    return result
print('\nOriginal Dictionary:')
print(dictt)
print('\nShortest list of values with the keys of the said dictionary:')
print(test(dictt))