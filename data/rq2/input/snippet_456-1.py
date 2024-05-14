from array import array

def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n
print('Original array:', nums)
nums_arr = list(map(int, nums))
result = array_sum(nums_arr)
print('Sum of all elements of the said array:')
print(result)