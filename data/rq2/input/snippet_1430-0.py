from collections import Counter
from itertools import chain
print('Original list of lists:')
print(nums)
print('\nFrequency of the elements in the said list of lists:')
result = Counter(chain.from_iterable(nums))
print(result)