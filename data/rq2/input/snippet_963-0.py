import numpy as np

def sum_matrix_Elements(m):
    arra = np.array(m)
    element_sum = 0
    for p in range(len(arra)):
        for q in range(len(arra[p])):
            if arra[p][q] == 0 and p < len(arra) - 1:
                arra[p + 1][q] = 0
            element_sum += arra[p][q]
    return element_sum
print('Original matrix:')
print(m)
print('Sum:')
print(sum_matrix_Elements(m))