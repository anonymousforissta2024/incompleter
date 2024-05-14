def avgfun(*n):
    sums = 0
    for t in n:
        sums = sums + t
    avg = sums / len(n)
    return avg
result1 = avgfun(1, 2, 3)
print(round(result1, 2))
print(round(result2, 2))