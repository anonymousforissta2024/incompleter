import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])
print('Sorted indices:')
print(indices)
print('Sorted data:')
for n in indices:
    print(student_id[n], student_height[n])