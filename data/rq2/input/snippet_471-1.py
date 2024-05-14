import pandas as pd
print('Original DataFrame:')
print(df)
print("\nMultiIndex using columns 't_id', ‘school_code’ and 'class':")
df1 = df.set_index(['t_id', 'school_code', 'class'])
print(df1)
print('\nConvert 1st and 3rd levels in the index frame into columns:')
df2 = df1.reset_index(level=['t_id', 'class'])
print(df2)