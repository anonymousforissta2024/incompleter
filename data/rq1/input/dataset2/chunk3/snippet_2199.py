#Source: https://stackoverflow.com/questions/51918256/python-merge-sort-typeerror-at-runtime
l=[int(n) for n in input().split()]

def merge_sort(l):
    if len(l)==1:
        return l
    else:
        a=l[:len(l)//2]
        b=l[len(l)//2:]
        print(a,b)
        a=merge_sort(a)
        b=merge_sort(b)
        j=0
        k=0

        for i in range(0,len(l)):
            if  a[j] < b[k]:
                l[i]=a[j]
                j+=1
                if j==len(a):
                    l=l.append(b[k:])
                    break
            else:
                l[i]=b[k]
                k+=1
                if k==len(b):
                    l=l.append(a[j:])
                    break
        # print(l)
        return l

print(merge_sort(l))