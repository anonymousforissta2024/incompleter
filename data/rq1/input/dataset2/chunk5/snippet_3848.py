#Source: https://stackoverflow.com/questions/47715318/typeerror-iter-returned-non-iterator-of-type-layer-for-python-3
net = nx.DiGraph()
print(path)
shp = ogr.Open(path)
for lyr in shp:
    print (type(lyr))
    print (lyr)
    fields = [x.GetName() for x in lyr.schema]
    print (lyr.schema)
    print(fields)
    for f in lyr:
        print(f)