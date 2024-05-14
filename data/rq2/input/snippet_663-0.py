def list_of_dicts(marks):
    keys = marks.keys()
    vals = zip(*[marks[k] for k in keys])
    result = [dict(zip(keys, v)) for v in vals]
    return result
print('Original dictionary of lists:')
print(marks)
print('\nSplit said dictionary of lists into list of dictionaries:')
print(list_of_dicts(marks))