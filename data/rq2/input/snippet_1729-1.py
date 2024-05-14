def power(N, P):
    if P == 0:
        return 1
    elif P == 1:
        return N
    else:
        return N * power(N, P - 1)
N = 5
print(power(N, P))