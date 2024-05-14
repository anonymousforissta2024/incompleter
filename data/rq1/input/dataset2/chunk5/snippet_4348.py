#Source: https://stackoverflow.com/questions/50939402/typeerror-range-object-does-not-support-item-assignment-how-to-fix-this
avail = range(n_connections)
for i in range(0,n_entities):
    for j in range(0,n_connections):
        if avail[j] != -1: #checking availability
            if (((dat[j][1] == 1)|((dat[j][1] == 11))) & (dat[j][2] == i)):
                if ((dat[j][3] == 3)|(dat[j][3] == 13)):
                    avail[j] = -1 # here error is coming how to fix this 
                   # n_connections = len(connectionx - 1)
                    for k in range (0,n_connections):
                        if avail[k] != -1: #checking availability
                            if (((dat[k][1] == 3)|((dat[k][1] == 13))) & (dat[k][2] == dat[j][4])):
                                avail[k] = -1 # booking