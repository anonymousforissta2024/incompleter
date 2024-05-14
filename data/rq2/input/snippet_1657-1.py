def Merge(dict1, dict2):
    return dict2.update(dict1)
dict1 = {'a': 10, 'b': 8}
print(Merge(dict1, dict2))
print(dict2)