def test(dictt, key, value):
    if any((sub[key] == value for sub in dictt)):
        return True
    return False
print('\nOriginal dictionary:')
print(students)
print('\nCheck if a specific Key and a value exist in the said dictionary:')
print(test(students, 'student_id', 1))
print(test(students, 'name', 'Brian Howell'))
print(test(students, 'class', 'VII'))
print(test(students, 'class', 'I'))
print(test(students, 'name', 'Brian Howelll'))
print(test(students, 'student_id', 11))