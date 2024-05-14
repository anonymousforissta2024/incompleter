import time
import numpy as np
SIZE = 200000
list1 = range(SIZE)
list2 = range(SIZE)
arra1 = np.arange(SIZE)
arra2 = np.arange(SIZE)
result = [(x, y) for x, y in zip(list1, list2)]
print('Time to aggregates elements from each of the iterables:')
print('List:')
print((time.time() - start_list) * 1000)
start_array = time.time()
result = arra1 + arra2
print('NumPy array:')
print((time.time() - start_array) * 1000)