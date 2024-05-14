import itertools

def findsubsets(s, n):
    return list(itertools.combinations(s, n))
n = 2
print(findsubsets(s, n))