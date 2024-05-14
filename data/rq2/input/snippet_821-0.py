def test(dictt, keys):
    return [list((d[k] for k in keys)) for d in dictt]
print('\nOriginal Dictionary:')
print(students)
print('\nExtract values from the said dictionarie and create a list of lists using those values:')
print('\n', test(students, ('student_id', 'name', 'class')))
print('\n', test(students, ('student_id', 'name')))
print('\n', test(students, ('name', 'class')))