def sort_sublists(input_list):
    result = [sorted(x, key=lambda x: x[0]) for x in input_list]
    return result
print('\nOriginal list:')
print(color1)
print('\nAfter sorting each sublist of the said list of lists:')
print(sort_sublists(color1))