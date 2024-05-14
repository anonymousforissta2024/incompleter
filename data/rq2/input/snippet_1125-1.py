def test(lst, marks):
    result = [d[marks] for d in lst if marks in d]
    return result
print('\nOriginal Dictionary:')
print(marks)
subj = 'Science'
print('\nExtract a list of values from said list of dictionaries where subject =', subj)
print(test(marks, subj))
print('\nOriginal Dictionary:')
print(marks)
subj = 'Math'
print('\nExtract a list of values from said list of dictionaries where subject =', subj)
print(test(marks, subj))