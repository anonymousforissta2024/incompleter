from bisect import bisect_left

def Binary_Search(l, x):
    i = bisect_left(l, x)
    if i:
        return i - 1
    else:
        return -1
x = 5
num_position = Binary_Search(nums, x)
if num_position == -1:
    print('Not found..!')
else:
    print('Largest value smaller than ', x, ' is at index ', num_position)