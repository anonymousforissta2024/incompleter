import numpy as np
first_names = ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')
x = np.lexsort((first_names, last_names))
print(x)