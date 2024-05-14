def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    else:
        return quick_sort([el for el in nums[1:] if el <= nums[0]]) + [nums[0]] + quick_sort([el for el in nums[1:] if el > nums[0]])
print('\nOriginal list:')
print(nums)
print('After applying Recursive Quick Sort the said list becomes:')
print(quick_sort(nums))
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print('\nOriginal list:')
print(nums)
print('After applying Recursive Quick Sort the said list becomes:')
print(quick_sort(nums))
nums = [1.1, 1, 0, -1, -1.1, 0.1]
print('\nOriginal list:')
print(nums)
print('After applying Recursive Quick Sort the said list becomes:')
print(quick_sort(nums))