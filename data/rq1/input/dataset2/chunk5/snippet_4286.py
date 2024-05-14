#Source: https://stackoverflow.com/questions/61125518/is-there-a-way-to-get-the-sum-of-non-zero-elements-in-numpy-array-i-keep-gettin
result=[]
FracPos = np.array(result)
for x in lines:
    result.append(x.split())
TotalCells = np.array(result)[:,2]
print(type(TotalCells))
print(type(FracPos))
FracPos = np.sum((TotalCells)>0)