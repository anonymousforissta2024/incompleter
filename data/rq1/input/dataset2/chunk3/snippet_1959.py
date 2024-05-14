#Source: https://stackoverflow.com/questions/52285972/unexpected-typeerror-nonetype-object-is-not-callable
A = np.random.randint(0,100,size=(100, 100))
B = np.random.randint(0,100,size=(100, 100))
def contrast(a, b):
    res = np.sum(np.equal(a, b))/(A.size)
    return res

res = contrast(A, B)
print("The correct rate is: %f"%res)