import numpy as np
last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')
x = np.lexsort((first_names, last_names))
print(x)