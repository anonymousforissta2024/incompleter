from itertools import groupby

def encode_list(s_list):
    return [[len(list(group)), key] for key, group in groupby(s_list)]
print('Original list:')
print(n_list)
print('\nList reflecting the run-length encoding from the said list:')
print(encode_list(n_list))
n_list = 'automatically'
print('\nOriginal String:')
print(n_list)
print('\nList reflecting the run-length encoding from the said string:')
print(encode_list(n_list))