import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
indices = np.lexsort((student_id, student_height))
print('Sorted indices:')
print(indices)
print('Sorted data:')
for n in indices:
    print(student_id[n], student_height[n])