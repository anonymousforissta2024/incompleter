import pandas as pd
n = 3
Sample_1 = [57, 51, 6]
Sample_2 = [92, 16, 19]
Sample_3 = [15, 93, 71]
Sample_4 = [28, 73, 31]
sample_id = zip(['S'] * n, list(range(1, n + 1)))
s_names = [''.join([w[0], str(w[1])]) for w in sample_id]
d = {'s_names': s_names, 'Sample_1': Sample_1, 'Sample_2': Sample_2, 'Sample_3': Sample_3, 'Sample_4': Sample_4}
mapping = {'Sample_1': 'Result_1', 'Sample_2': 'Result_1', 'Sample_3': 'Result_2', 'Sample_4': 'Result_2'}
df = df_1.set_index('s_names').groupby(mapping, axis=1).sum()
df.reset_index(level=0)