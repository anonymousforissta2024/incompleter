print('Original Dictionary:')
print(dict1)
print('New Dictionary after dropping empty items:')
dict1 = {key: value for key, value in dict1.items() if value is not None}
print(dict1)