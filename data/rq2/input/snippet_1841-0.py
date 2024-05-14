import pandas as pd
import numpy as np
column = ['a', 'b', 'c', 'd', 'e']
index = ['A', 'B', 'C', 'D', 'E']
print(df1)
print('\n\nDataframe after reindexing rows: \n', df1.reindex(['B', 'D', 'A', 'C', 'E']))