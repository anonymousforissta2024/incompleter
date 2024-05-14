from bisect import bisect_left

def Binary_Search(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
nums = [1, 2, 3, 4, 8, 8, 10, 12]
num_position = Binary_Search(nums, x)
if num_position == -1:
    print(x, 'is not present.')
else:
    print('First occurrence of', x, 'is present at index', num_position)