from collections import OrderedDict
print('Original String:')
print(text_str)
print('\nAfter removing duplicate words from the said string:')
result = ' '.join(OrderedDict(((w, w) for w in text_str.split())).keys())
print(result)