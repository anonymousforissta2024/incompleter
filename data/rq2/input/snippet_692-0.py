def reverse_list_of_lists(nums, lr, hr):
    temp = []
    for idx, el in enumerate(nums):
        if idx >= lr and idx < hr:
            temp.append(el)
    result_max = max(temp)
    result_min = min(temp)
    return (result_max, result_min)
print('Original list:')
print(nums)
print('\nIndex range:')
lr = 3
hr = 8
print(lr, 'to', hr)
print('\nMaximum and minimum values of the said given list within index range:')
print(reverse_list_of_lists(nums, lr, hr))