import numpy as np
print('initial array : ', str(ini_array))
result = ini_array[ini_array != ini_array.astype(int)]
print('final array', result)