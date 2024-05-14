#Source: https://stackoverflow.com/questions/62768022/typeerror-zip-argument-1-must-support-iteration-in-python
df1=pd.DataFrame({'A':[1,3,4,7,8,11,1,15,20,15,16,87],
                     'B':[1,3,4,6,8,11,1,19,20,15,16,87],
                     'flag':[0,0,0,0,1,1,1,0,0,1,0,0]})

for item in idx:
    N = 2
    s = [x for s, e in zip(item-N,item) for x in range(s, e+1)]
    df_before_2rows=df1.loc[df1.index.intersection(s)]