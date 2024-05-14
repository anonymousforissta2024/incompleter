#Source: https://stackoverflow.com/questions/56980048/slice-indices-typeerror-and-insert-list-method-weird-behavior
a = [[0, 4]]
b = '1','2','3','4','5'
c = '*a3b*'

for f in b:
    if (f in c[a[0][0]:a[0][1]]):
        a[0].insert(0,f)