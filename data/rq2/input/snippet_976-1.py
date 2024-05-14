def sort_matrix(M):
    result = sorted(M, key=lambda matrix_row: sum(matrix_row))
    return result
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print('Original Matrix:')
print(matrix1)
print('\nSort the said matrix in ascending order according to the sum of its rows')
print(sort_matrix(matrix1))
print('\nOriginal Matrix:')
print(matrix2)
print('\nSort the said matrix in ascending order according to the sum of its rows')
print(sort_matrix(matrix2))