from itertools import groupby

def remove_all_consecutive(str1):
    result_str = []
    for key, group in groupby(str1):
        result_str.append(key)
    return ''.join(result_str)
print('Original string:' + str1)
print('After removing consecutive duplicates: ' + str1)
print(remove_all_consecutive(str1))