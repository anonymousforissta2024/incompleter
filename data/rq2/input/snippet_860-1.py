def sum_Range_list(nums, m, n):
    sum_range = 0
    for i in range(m, n + 1, 1):
        sum_range += nums[i]
    return sum_range
print('Original list:')
print(nums)
m = 8
n = 10
print('Range:', m, ',', n)
print('\nSum of the specified range:')
print(sum_Range_list(nums, m, n))