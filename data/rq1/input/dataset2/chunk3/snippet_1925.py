#Source: https://stackoverflow.com/questions/62973342/how-can-i-fix-this-error-typeerror-list-object-is-not-callable-on-line-17
def last_four(x):
    return x[-4:]
        

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
ids2=[]
for i in ids:
    ids2.append(str(i))
sorted_ids=sorted(ids2,key=last_four(ids2))
print(sorted_ids)