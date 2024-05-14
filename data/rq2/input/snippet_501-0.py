def test(flat_dict):
    return list(flat_dict.values())
print('\nOriginal dictionary elements:')
print(students)
print('\nCreate a flat list of all the values of the said flat dictionary:')
print(test(students))