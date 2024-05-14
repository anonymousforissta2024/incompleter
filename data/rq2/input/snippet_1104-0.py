def grouping_dictionary(l):
    result = {}
    for k, v in l:
        result.setdefault(k, []).append(v)
    return result
print('Original list:')
print(colors)
print('\nGrouping a sequence of key-value pairs into a dictionary of lists:')
print(grouping_dictionary(colors))