#Source: https://stackoverflow.com/questions/54965624/typeerror-unsupported-operand-types-for-int-and-tuple-error
a=[1,2,3,4,5]
for i in range(len(a)):
    sum=2
    for j in range(i):
        sum+=a[j]
    a[i]=(a[i],sum)
print(a)