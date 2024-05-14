import numpy as geek
print('Input array : ', in_arr)
num = 4
print('The number which we want to insert : ', num)
out_ind = geek.searchsorted(in_arr, num)
print('Output indices to maintain sorted array : ', out_ind)