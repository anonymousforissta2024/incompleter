from itertools import groupby

def extract_elements(nums, n):
    result = [i for i, j in groupby(nums) if len(list(j)) == n]
    return result
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
n = 2
print('Original list:')
print(nums1)
print('Extract 2 number of elements from the said list which follows each other continuously:')
print(extract_elements(nums1, n))
n = 4
print('Original lists:')
print(nums2)
print('Extract 4 number of elements from the said list which follows each other continuously:')
print(extract_elements(nums2, n))