def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
print('Original dictionary of lists:')
print(marks)
print('\nSplit said dictionary of lists into list of dictionaries:')
print(list_of_dicts(marks))