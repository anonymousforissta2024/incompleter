from collections import defaultdict

def grouping_dictionary(l):
    d = defaultdict(list)
    for k, v in l:
        d[k].append(v)
    return d
print('Original list:')
print(colors)
print('\nGrouping a sequence of key-value pairs into a dictionary of lists:')
print(grouping_dictionary(colors))