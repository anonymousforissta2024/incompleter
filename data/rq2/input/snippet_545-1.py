import numpy as np
student = '01\tV\tDebby Pramod\n02\tV\tArtemiy Ellie\n03\tV\tBaptist Kamal\n04\tV\tLavanya Davide\n05\tV\tFulton Antwan\n06\tV\tEuanthe Sandeep\n07\tV\tEndzela Sanda\n08\tV\tVictoire Waman\n09\tV\tBriar Nur\n10\tV\tRose Lykos'
print('Original text:')
print(student)
text_lines = [r.split('\t') for r in text_lines]
result = np.array(text_lines, dtype=np.str)
print('\nArray from the said text:')
print(result)