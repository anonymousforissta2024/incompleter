import numpy as np
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])
indices = np.lexsort((student_id, student_height))
print('Sorted indices:')
print(indices)
print('Sorted data:')
for n in indices:
    print(student_id[n], student_height[n])