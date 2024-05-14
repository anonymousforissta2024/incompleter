def extract_nth_element(test_list, n):
    result = [x[n] for x in test_list]
    return result
print('Original list:')
print(students)
n = 0
print('\nExtract nth element ( n =', n, ') from the said list of tuples:')
print(extract_nth_element(students, n))
n = 2
print('\nExtract nth element ( n =', n, ') from the said list of tuples:')
print(extract_nth_element(students, n))