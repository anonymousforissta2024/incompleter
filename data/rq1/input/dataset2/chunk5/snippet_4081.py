#Source: https://stackoverflow.com/questions/59414732/typeerror-can-only-concatenate-list-not-tuple-to-list
fde = fde[features]
locations = []
for row in fde.iterrows():
    temp_elite = fne[features]
    temp_elite = temp_elite.append(row)
    tree = KDTree(temp_elite, metric='euclidean')
    dist, ind = tree.query(temp_elite, k=4)
    print(ind)
    locations.append(ind.tail(1))
print(locations)