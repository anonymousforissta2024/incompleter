#Source: https://stackoverflow.com/questions/59417946/typeerror-int-object-is-not-callable-at-last-lne
l=[int(x) for x in "10,22,9,33,21,50,41,60,80".split(sep = ",")]
print(l)
length1 = [1 for i in range(len(l))]
for i in range(len(l)):
    max = l[i]
    for j in range(i+1,len(l)):
        if l[j]>max:
            max=l[j]
            length1[i]=length1[i]+1
print(max(length1))