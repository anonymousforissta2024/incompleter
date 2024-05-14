#Source: https://stackoverflow.com/questions/40559769/typeerror-cant-convert-module-object-to-str-implicitly
import pandas as pd
import csv
import os

#readfile
loandata=pd.DataFrame(pd.read_table('/Users/lixuefei/Desktop/Sample Dataset/test.txt',header = None,index_col=2))

#classify
volume_type=list(set(loandata[3]))
system_type=list(set(loandata[4]))
area_name=list(set(loandata[5]))

df=pd.DataFrame(loandata[(loandata[3]==volume_type[0])& (loandata[4]==system_type[0])&(loandata[5]==area_name[0])])
#set the file path
path='/Users/lixuefei/Desktop/Sample Dataset'
filename=volume_type[0]+system_type[0]+area_name[0]
filetype=csv

if not df.empty:
    df.to_csv(os.path.join(path,filename+filetype),header=None)
else:
    print("Empty")