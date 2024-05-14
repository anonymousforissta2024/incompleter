import numpy as np
np.random.seed(42)
print('Original array:')
print(student)
np.random.shuffle(student[2:8])
print('Shuffle the said array rows starting from 3rd to 9th')
print(student)