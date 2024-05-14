def Cloning(li1):
    li_copy = li1[:]
    return li_copy
li2 = Cloning(li1)
print('Original List:', li1)
print('After Cloning:', li2)