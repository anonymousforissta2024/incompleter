def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
dictionary = {}
print(Convert(tups, dictionary))