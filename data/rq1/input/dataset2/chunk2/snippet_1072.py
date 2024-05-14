#Source: https://stackoverflow.com/questions/74849766/typeerror-cannot-unpack-non-iterable-int-object-with-filter-function
liste = [(3,4,5),(6,8,10),(3,10,7)]

def ucgen_mi(s):
    for g in s:
        a, b, c = g
        if (a + b > c and a + c > b and c + b > a):
            return True
        else:
            return False


print(list(filter(ucgen_mi, liste)))