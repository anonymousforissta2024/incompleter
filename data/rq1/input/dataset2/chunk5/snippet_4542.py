#Source: https://stackoverflow.com/questions/64630972/typeerror-object-of-type-int-has-no-len-in-python
res = []

for x in range(9):

    if x == 0:
        res.append([1])
    elif x == 1:
        res.append([1,1])
        print(res)
    else:
        l=[]
        for y in range(len(res[x-1])):
            if y == 0:
                l.append(1)
            else:
                l.append(res[x-1][y] + res[x-1][y-1])
    l.append(1)
    res.append(1)