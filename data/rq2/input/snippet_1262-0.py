from bisect import bisect_right

def BinarySearch(a, x):
    i = bisect_right(a, x)
    if i != len(a) + 1 and a[i - 1] == x:
        return i - 1
    else:
        return -1
x = 8
num_position = BinarySearch(nums, x)
if num_position == -1:
    print('not presetn!')
else:
    print('Last occurrence of', x, 'is present at', num_position)