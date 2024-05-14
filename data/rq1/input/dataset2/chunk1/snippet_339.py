#Source: https://stackoverflow.com/questions/64472712/accessing-each-element-of-a-list-according-to-given-list-of-indexes-typeerror
index=[0, 1, 5, 6, 10, 11]
area=[78.0, 125.0, 203.0, 266.0, 344.0, 141.0, 46.0, 187.0, 245.0, 265.0, 78.0, 203.0]
key_to_del = False

for x in index:    
    for j in area:
        if float(j[x]) >150:
            print(j[x])
           