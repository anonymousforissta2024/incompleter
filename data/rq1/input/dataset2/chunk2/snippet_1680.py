#Source: https://stackoverflow.com/questions/65511540/attributeerror-list-object-attribute-append-is-read-only
dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

exceed2 = []

for d, i in enumerate(dbs):
    if i > 10:
        exceed2.append= (d,i)
        print(exceed2)