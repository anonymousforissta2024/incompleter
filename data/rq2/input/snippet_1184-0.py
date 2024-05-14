def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))
    return result
print('Original Dictionary:')
print(students)
print('\nHeight> 6ft and Weight> 70kg:')
print(filter_data(students))