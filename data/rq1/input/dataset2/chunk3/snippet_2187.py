#Source: https://stackoverflow.com/questions/63563886/type-error-a-def-that-works-only-with-str-but-not-int
def tiene_uno(expresion):
    n = str(len(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)