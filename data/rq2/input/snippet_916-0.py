print('original List:')
print(nums1)
print('\nRotate the said list in left direction by 4:')
result = nums1[3:] + nums1[:4]
print(result)
print('\nRotate the said list in left direction by 2:')
result = nums1[2:] + nums1[:2]
print(result)
print('\nRotate the said list in Right direction by 4:')
result = nums1[-3:] + nums1[:-4]
print(result)
print('\nRotate the said list in Right direction by 2:')
result = nums1[-2:] + nums1[:-2]
print(result)