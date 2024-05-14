import itertools

def findsubsets(s, n):
    return list(itertools.combinations(s, n))
s = {1, 2, 3}
print(findsubsets(s, n))