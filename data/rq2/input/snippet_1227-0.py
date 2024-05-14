def test(dictt, N):
    result = sorted(dictt, key=dictt.get, reverse=True)[:N]
    return result
print('\nOriginal Dictionary:')
print(dictt)
N = 1
print('\n', N, 'maximum value(s) in the said dictionary:')
print(test(dictt, N))
N = 2
print('\n', N, 'maximum value(s) in the said dictionary:')
print(test(dictt, N))
N = 5
print('\n', N, 'maximum value(s) in the said dictionary:')
print(test(dictt, N))