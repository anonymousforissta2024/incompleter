import pandas as pd
print('Sequences of fixed-frequency dates and time spans (1 H):\n')
r1 = pd.date_range('2030-01-01', periods=10, freq='H')
print(r1)
print('\nSequences of fixed-frequency dates and time spans (3 H):\n')
print(r2)