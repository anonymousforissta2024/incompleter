def test(lsts, key):
    return [x.get(key) for x in lsts]
print('Original list of dictionaries:')
print(students)
print('\nConvert a list of dictionaries into a list of values corresponding to the specified key:')
print(test(students, 'age'))