#Source: https://stackoverflow.com/questions/53027316/pulp-typeerror-can-only-add-lpconstraintvar-lpconstraint-lpaffineexpression
for i in range(I):
    for j in range(J):
        for k in range(K):
            model += A[i] >= j * x[i, j, k]