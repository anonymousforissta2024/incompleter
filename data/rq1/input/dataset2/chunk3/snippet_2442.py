#Source: https://stackoverflow.com/questions/58256867/attributeerror-dataframe-object-has-no-attribute-net-name
import csv
import os
import pandas as pd
import datetime
import numpy as np

from time import gmtime, strftime
WCOUNT=strftime("%V", gmtime())
WCOUNT = int(WCOUNT)
WCOUNT_last = int(WCOUNT)-1
os.environ['NLS_LANG'] = 'Russian.AL32UTF8'

cell_file_list=pd.read_excel('cdt_config.xlsx',sheet_name ='cdt_config',index_col='para_name')
filial_name_list=pd.read_excel('FILIAL_NAME.xlsx')
gcell_file_name1=cell_file_list.para_value.loc['ucell_file_name']
ecell_file_name=cell_file_list.para_value.loc['ecell_file_name']
cols_simple=['RECDATE','REGION_PHOENIX_NAME','NET_NAME','CELL_NAME_IN_BSC','ENODEB_NAME','ECELL_TYPE','NRI_ADDRESS', 'NRI_BS_NUMBER','NRI_SITEID','STOPTIME',  ]
cols_export=['GSM', 'UMTS', 'LTE', 'TOTAL', 'NWEEK', 'SHARING' ]
ecell_df=df = pd.read_csv(ecell_file_name, sep=",",encoding='cp1251',
                dtype={'NRI_SITEID': str})

ecell_df=ecell_df.rename(columns={"RECDATE.DATE": "RECDATE"})
ecell_df=ecell_df.rename(columns={"ECELL_MNEMONIC": "CELL_NAME_IN_BSC"})

#replace ","
ecell_df.STOPTIME=pd.to_numeric(ecell_df.STOPTIME.replace(',', '', regex=True), errors='coerce')/3600
ecell_df=ecell_df[cols_simple]
#pivot ecell table
ecell_sum_df=pd.pivot_table(ecell_df,values='STOPTIME',index=['RECDATE','NRI_SITEID','REGION_PHOENIX_NAME','NET_NAME','ENODEB_NAME','ECELL_TYPE'],aggfunc='sum')
ecell_sum_df=ecell_sum_df.fillna(0)
#create a empty column with the same index as the pivot table.
ecell_export_df= pd.DataFrame(index=ecell_sum_df.index.copy())
ecell_export_df=ecell_export_df.assign(LTE=0)
ecell_export_df.LTE=ecell_sum_df.STOPTIME
ecell_export_df['SHARING'] = 0
ecell_export_df.SHARING.replace(ecell_export_df.NET_NAME in filial_name_list, ENODEB_NAME,inplace=True)
print(ecell_export_df)
#print (ecell_export_df)
del ecell_df
del ecell_sum_df

export_df=pd.concat([ecell_export_df],join='outer',axis=1)
export_df=export_df.fillna(0)
export_df['TOTAL'] = export_df.sum(axis=1)
export_df['NWEEK'] = WCOUNT_last

del ecell_export_df
#################################################