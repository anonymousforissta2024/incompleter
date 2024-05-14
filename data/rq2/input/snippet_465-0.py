import numpy as np
np.set_printoptions(linewidth=100)
student = np.array([['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
print('Original array:')
print(student)
char = 'E'
print('\nStudent name starting with', char, ':')
print(result)
char = '1'
result = student[np.char.startswith(student[:, 0], char)]
print('\nStudent id starting with', char, ':')
print(result)