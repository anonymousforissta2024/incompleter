import numpy as np
np.set_printoptions(linewidth=100)
student = np.array([['01', 'V', 'Debby Pramod', 30.21], ['02', 'V', 'Artemiy Ellie', 29.32], ['03', 'V', 'Baptist Kamal', 31.0], ['04', 'V', 'Lavanya Davide', 30.22], ['05', 'V', 'Fulton Antwan', 30.21], ['06', 'V', 'Euanthe Sandeep', 31.0], ['07', 'V', 'Endzela Sanda', 32.0], ['08', 'V', 'Victoire Waman', 29.21], ['09', 'V', 'Briar Nur', 30.0], ['10', 'V', 'Rose Lykos', 32.0]])
print('Original array:')
print(student)
result = student[np.char.startswith(student[:, 2], char)]
print('\nTotal weight, where student name starting with', char)
print(np.round(result[:, 3].astype(float).sum(), 2))
char = 'D'
result = student[np.char.startswith(student[:, 2], char)]
print('\nTotal weight, where student name starting with', char)
print(np.round(result[:, 3].astype(float).sum(), 2))