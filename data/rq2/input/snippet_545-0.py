import numpy as np
print('Original text:')
print(student)
text_lines = student.splitlines()
text_lines = [r.split('\t') for r in text_lines]
result = np.array(text_lines, dtype=np.str)
print('\nArray from the said text:')
print(result)