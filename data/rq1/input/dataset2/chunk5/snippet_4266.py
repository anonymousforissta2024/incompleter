#Source: https://stackoverflow.com/questions/45479406/transferring-int-values-into-dict-typeerror-int-object-is-not-subscriptable
fwd = {1:1, 2:10, 3:100, 5:10000, 103: 103, 204:204, 205:205, 387:387}


fragment_dic = {}
count = 0

for fragment_num in range(0, 388, 1):
    for pos in range(1,101, 1):
        if fwd == int:
            print()
            genomic_position = fragment_num*100 + pos
            count += fwd[genomic_position] 
        elif fwd != int:
            pass
        fragment_dic[fragment_num] = count
        count = 0
        for i in fwd:    
            fwd[fragment_dic] = i[0]