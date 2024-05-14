#Source: https://stackoverflow.com/questions/55551721/getting-typeerror-of-tuple-even-though-the-object-is-of-type-numpy-nparray
labels=np.ones(length,dtype=int)
print(type(labels))
labels[:43]=0
labels[43:263]=1
labels[263:]=2
print(labels.shape())#produces error