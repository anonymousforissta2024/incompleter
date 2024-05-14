def count_occurrences(nums):
    result = dict(map(lambda el: (el, list(nums).count(el)), nums))
    return result
print('Original list:')
print(nums)
print('\nCount the occurrences of the items in the said list:')
print(count_occurrences(nums))