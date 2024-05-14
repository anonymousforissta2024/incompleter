def test(lst):
    result = {item[0]: item[1:] for item in lst}
    return result
print('\nOriginal list of lists:')
print(students)
print('\nConvert the said list of lists to a dictionary:')
print(test(students))