#Source: https://stackoverflow.com/questions/18282148/why-does-my-code-produce-typeerror-nonetype-object-is-not-iterable
def merge( s1, s2):
    if len(s1) == 0:
        return s2[:]
    if len(s2) == 0:
        return s1[:]
    minElm = []
    if s1[0] <= s2[0]:
        minElm.append( s1.pop(0) )
    else:
        minElm.append( s2.pop(0) )
    return minElm.extend( merge(s1[:], s2[:] ))

list1 = [1,3,5,7,9]
list2 = [2,4,6,8]

merged = merge( list1[:], list2[:] )
print(merged)