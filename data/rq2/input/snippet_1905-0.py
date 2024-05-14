import bisect
print('The rightmost index to insert, so list remains sorted is  : ', end='')
print(bisect.bisect(li, 4))
print('The leftmost index to insert, so list remains sorted is  : ', end='')
print(bisect.bisect_left(li, 4))
print('The rightmost index to insert, so list remains sorted is  : ', end='')
print(bisect.bisect_right(li, 4, 0, 4))