from collections import Counter
from itertools import chain

def max_aggregate(list_str, N):
    temp = (set(sub) for sub in list_str)
    counts = Counter(chain.from_iterable(temp))
    gt_N = [chr for chr, count in counts.items() if count > N]
    lt_N = [chr for chr, count in counts.items() if count < N]
    return (gt_N, lt_N)
list_str = ['abcd', 'iabhef', 'dsalsdf', 'sdfsas', 'jlkdfgd']
print('Original list:')
print(list_str)
result = max_aggregate(list_str, N)
print('\nCharacters of the said list of strings which occur more than:', N)
print(result[0])
print('\nCharacters of the said list of strings which occur less than:', N)
print(result[1])