import pandas as pd
import numpy as np
print('Original series:')
print(num_series)
autocorrelations = [num_series.autocorr(i).round(2) for i in range(11)]
print('\nAutocorrelations of the said series:')
print(autocorrelations[1:])