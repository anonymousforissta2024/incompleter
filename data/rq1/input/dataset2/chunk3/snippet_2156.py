#Source: https://stackoverflow.com/questions/52285972/unexpected-typeerror-nonetype-object-is-not-callable
@gettime
def contrast(a, b):
    res = np.sum(np.equal(a, b))/len(a)
    return res

res = contrast(A, B)
print("The correct rate is: %f"%res)