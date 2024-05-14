def Merge(dict1, dict2):
    return dict2.update(dict1)
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2))
print(dict2)