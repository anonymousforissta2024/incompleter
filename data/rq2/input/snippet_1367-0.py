def reverse_list_lists(nums):
    for l in nums:
        l.sort(reverse=True)
    return nums
print('Original list of lists:')
print(nums)
print('\nReverse each list in the said list of lists:')
print(reverse_list_lists(nums))