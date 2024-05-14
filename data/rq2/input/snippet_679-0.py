import itertools as it

def list_max_min_pair(nums):
    result_max = max(it.combinations(nums, 2), key=lambda sub: sub[0] * sub[1])
    result_min = min(it.combinations(nums, 2), key=lambda sub: sub[0] * sub[1])
    return (result_max, result_min)
print('The original list: ')
print(nums)
print('\nPairs of maximum and minimum product from the said list:')
print(list_max_min_pair(nums))