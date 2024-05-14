#Source: https://stackoverflow.com/questions/70348607/typeerror-unsupported-operand-types-for-str-and-str-pandas-reindex
import pandas as pd
s1=pd.Series([1,2,3,4],index=list('aceg'))
print(s1.reindex(pd.Index(list('abdg')),method='nearest'))