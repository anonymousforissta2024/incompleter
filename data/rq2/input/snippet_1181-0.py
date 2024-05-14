from array import *
print('Original array: ' + str(array_num))
print('Current memory address and the length in elements of the buffer: ' + str(array_num.buffer_info()))
print('The size of the memory buffer in bytes: ' + str(array_num.buffer_info()[1] * array_num.itemsize))