def filter_data(students):
    result = {k: s for k, s in students.items() if s[0] >= 6.0 and s[1] >= 70}
    return result
print('Original Dictionary:')
print(students)
print('\nHeight > 6ft and Weight> 70kg:')
print(filter_data(students))