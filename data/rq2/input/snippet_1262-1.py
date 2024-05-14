from bisect import bisect_right

def BinarySearch(a, x):
    i = bisect_right(a, x)
    if i != len(a) + 1 and a[i - 1] == x:
        return i - 1
    else:
        return -1
nums = [1, 2, 3, 4, 8, 8, 10, 12]
x = 8
if num_position == -1:
    print('not presetn!')
else:
    print('Last occurrence of', x, 'is present at', num_position)