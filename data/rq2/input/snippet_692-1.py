def reverse_list_of_lists(nums, lr, hr):
    temp = []
    for idx, el in enumerate(nums):
        if idx >= lr and idx < hr:
            temp.append(el)
    result_max = max(temp)
    result_min = min(temp)
    return (result_max, result_min)
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
print('Original list:')
print(nums)
print('\nIndex range:')
hr = 8
print(lr, 'to', hr)
print('\nMaximum and minimum values of the said given list within index range:')
print(reverse_list_of_lists(nums, lr, hr))