def top_product(nums1, nums2, N):
    result = sorted([x * y for x in nums1 for y in nums2], reverse=True)[:N]
    return result
nums2 = [3, 6, 8, 9, 10, 6]
print('Original lists:')
print(nums1)
print(nums2, '\n')
N = 3
print(N, 'Number of largest products from the said two lists:')
print(top_product(nums1, nums2, N))
N = 4
print(N, 'Number of largest products from the said two lists:')
print(top_product(nums1, nums2, N))