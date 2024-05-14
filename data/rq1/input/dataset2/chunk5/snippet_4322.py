#Source: https://stackoverflow.com/questions/37398907/for-x-in-l-for-each-item-at-this-level-typeerror-int-object-is-not-iterabl
def sumtree(L):
    tot = 0
    for x in L:  # For each item at this level
        if not isinstance(x,list):
            tot += x  # Add numbers directly
    else:
       tot += sumtree(x)  # Recur for sublists
    return tot

l1 = [1, 2, 3, 4, [23, 33, [22, 22], 12, [12, 11]]]
print(sumtree(l1))