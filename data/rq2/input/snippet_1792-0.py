import numpy as geek
print('Input array  : ', arr)
print('First order difference  : ', geek.diff(arr))
print('Second order difference : ', geek.diff(arr, n=2))
print('Third order difference  : ', geek.diff(arr, n=3))