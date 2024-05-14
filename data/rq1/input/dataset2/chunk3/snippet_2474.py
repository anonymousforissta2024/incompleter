#Source: https://stackoverflow.com/questions/64816017/typeerror-function-object-is-not-subscriptable-while-the-error-line-is-worki
def DESCRYSubAESHex(SubHex1, FullKey):

    #print(SubHex1)
    #print(FullKey)
    for a in range(16):
        #print(SubHex1[a])
        #print(FullKey[0][a])
        SubHex1[a] = xor_strings(SubHex1[a],FullKey[len(FullKey) - 1][a])         

    for a in range(len(FullKey) - 2):  # 0 to 13
        #print(SubHex1)
        SubHex1 = ReVerseShiftRowMK2(SubHex1)
       

        SubHex1 = reVeredSBox(SubHex1)

      

        for b in range(16):
            SubHex1[b] = xor_strings(SubHex1[b],FullKey[(len(FullKey) - 2) - a][b])       
        
        SubHex1 = reVersedMixCol

    SubHex1 = ReVerseShiftRowMK2(SubHex1)

    SubHex1 = reVeredSBox(SubHex1)

    for b in range(16):
        SubHex1[b] = xor_strings(SubHex1[b],FullKey[0][b]) 

    

    return SubHex1

print(DESCRYSubAESHex(S, A))