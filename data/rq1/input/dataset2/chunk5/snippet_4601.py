#Source: https://stackoverflow.com/questions/66767714/typeerror-int-object-is-not-iterable-in-a-for-loop
import random

def compte(l,v):
    nbreOccurences = 0
    for i in l:
        if (i == v):
            nbreOccurences = nbreOccurences + 1
    return nbreOccurences

N = 100
            
l3 = []
for i in range(N):
    v = random.randrange(1,N+1)
    l3.append(v)

print(l3)
print(compte(13,3))            