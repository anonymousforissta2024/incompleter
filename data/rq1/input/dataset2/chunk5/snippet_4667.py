#Source: https://stackoverflow.com/questions/63373834/typeerror-can-only-concatenate-str-not-nonetype-to-str-on-recursive-functio
def NumberToSymbol(r):
    nuc={0:"A", 1:"C", 2:"G",3:"T"}
    return nuc.get(r)
def NumberToPattern(index, k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex=index/ 4
    r = index % 4
    symbol=NumberToSymbol(r)
    PrefixPattern =NumberToPattern(prefixIndex, k-1)
    return  PrefixPattern+ symbol

print(NumberToPattern(45,4))