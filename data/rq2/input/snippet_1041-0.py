from collections import defaultdict

def max_occurrences(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1])
    return result
print('Original list:')
print(nums)
print('\nItem with maximum frequency of the said list:')
print(max_occurrences(nums))