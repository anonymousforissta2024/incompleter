#Source: https://stackoverflow.com/questions/54402080/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-when-s
import pandas as pd
from pybloqs import Block, html
import pybloqs.block.table_formatters as tf

d = {'one': [1., 2., 3., 4.],
 'two': [4., 3., 2., 1.]}

df  =  pd.DataFrame(d)

block_df =  Block(df, formatters=None, use_default_formatters=True)
block_df.save('test.pdf')