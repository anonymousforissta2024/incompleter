print('Original list:')
print(text)
print('\nDisplay each element vertically of the said list:')
for i in text:
    print(i)
nums = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
print('Original list:')
print(nums)
print('\nDisplay each element vertically of the said list of lists:')
for a, b, c in zip(*nums):
    print(a, b, c)