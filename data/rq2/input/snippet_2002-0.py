import numpy as np
from ast import literal_eval
print('Type of name_list created:\n', type(name_list))
t = literal_eval(name_list)
print('\nPrinting the original Name_list dictionary:\n', t)
print('Type of original dictionary:\n', type(t))
result_nparra = np.array([[v[j] for j in ['First_Name', 'Second_Name', 'Interest']] for k, v in t.items()])
print('\nConverted ndarray from the Original dictionary:\n', result_nparra)
print('Type:\n', type(result_nparra))