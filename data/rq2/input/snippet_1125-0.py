def test(lst, marks):
    result = [d[marks] for d in lst if marks in d]
    return result
marks = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
print('\nOriginal Dictionary:')
print(marks)
print('\nExtract a list of values from said list of dictionaries where subject =', subj)
print(test(marks, subj))
print('\nOriginal Dictionary:')
print(marks)
subj = 'Math'
print('\nExtract a list of values from said list of dictionaries where subject =', subj)
print(test(marks, subj))