text = ['a', 'b', 'c', 'd', 'e', 'f']
print('Original list:')
print(text)
print('\nDisplay each element vertically of the said list:')
for i in text:
    print(i)
print('Original list:')
print(nums)
print('\nDisplay each element vertically of the said list of lists:')
for a, b, c in zip(*nums):
    print(a, b, c)