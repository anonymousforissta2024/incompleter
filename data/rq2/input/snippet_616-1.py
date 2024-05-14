from collections import Counter
print('Original list of tuples:')
print(nums)
result = Counter((tuple(sorted(i)) for i in nums[0]))
print('\nTuples', '    ', 'frequency')
for key, val in result.items():
    print(key, ' ', val)