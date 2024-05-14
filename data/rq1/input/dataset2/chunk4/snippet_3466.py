#Source: https://stackoverflow.com/questions/64509096/typeerror-not-supported-between-instances-of-numpy-ndarray-and-str-when
maxcoord = [0,0,0,0,0,0]
mincoord = [0,0,0,0,0,0]
for i in range(num_atoms):
    if(coord_array[i][0] > maxcoord[0]):
        maxcoord[0] = coord_array[i][0]
        maxcoord[1] = names[i]
    if(coord_array[i][0] < mincoord[0]):
        mincoord[0] = coord_array[i][0]
        mincoord[1] = names[i]
    if(coord_array[i][1] > maxcoord[2]):
        maxcoord[2] = coord_array[i][1]
        maxcoord[2] = names[i]
    if(coord_array[i][1] < mincoord[2]):
        mincoord[2] = coord_array[i][1]
        mincoord[2] = names[i]
    if(coord_array[i][2] > maxcoord[4]):
        maxcoord[4] = coord_array[i][2]
        maxcoord[5] = names[i]
    if(coord_array[i][2] < mincoord[4]):
        mincoord[4] = coord_array[i][2]
        mincoord[5] = names[i]