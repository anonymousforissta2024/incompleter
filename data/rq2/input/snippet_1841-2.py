import pandas as pd
import numpy as np
index = ['A', 'B', 'C', 'D', 'E']
df1 = pd.DataFrame(np.random.rand(5, 5), columns=column, index=index)
print(df1)
print('\n\nDataframe after reindexing rows: \n', df1.reindex(['B', 'D', 'A', 'C', 'E']))