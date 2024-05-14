#Source: https://stackoverflow.com/questions/38146756/typeerror-cant-convert-io-textiowrapper-object-to-str-implicitly
import numpy as np
import pandas as pa

# opening the file
dossier = "Plip"
fichier = "plop.txt"
fichier = open(dossier + "/" + fichier)
data = fichier.readlines()

# creating the data frame
Pair = []
Impair = []
for m in data:
    impair = int(m[0:1])
    pair = int(m[2:3])
    Impair.append(impair)
    Pair.append(pair)

M = np.array([Impair, Pair]).transpose()
Table = pa.DataFrame(M, columns = ["Impair", "Pair"])

#creating the .csv file
Table.to_csv(dossier + fichier + ".csv")