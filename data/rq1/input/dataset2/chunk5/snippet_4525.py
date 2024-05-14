#Source: https://stackoverflow.com/questions/51621735/pandas-feeding-slice-as-pandas-core-indexes-numeric-int64index-getting-typeerror
import pandas as pd

data = [['edward',1],['edward',0],['edward',0],['norm',1],['norm',0],['norm',0] ]

df_names = pd.DataFrame( data )

criteria = df_names[1] == 1

df_just_changes = df_names[ criteria ]

print(df_names)
print(df_just_changes .index)
print("type of  df_just_changes.index {} ".format(type( df_just_changes.index ) ) )
print("type of  df_just_changes.index[0] {} ".format(type( df_just_changes.index[0] ) ) )
print( df_names.values[df_just_changes.index : 2 ])