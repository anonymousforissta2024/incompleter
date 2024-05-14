#Source: https://stackoverflow.com/questions/42178236/typeerror-unsupported-operand-types-for-nonetype-and-int-python-3
decimaal = 0


# Laat de gebruiker een waarde in typen
def user_input():
    getal = int(input('Geef het getal: '))
    if getal < 10000:
        return getal
    else:
        print('Het getal moet kleiner zijn dan 10.000!')
        user_input()


# functie om getal in het decimaal- naar octaal-stelsel om te zetten
def decimaal_octaal_converter(decimaal):
    resultaat = []
    quotient = decimaal
    rest = 0

    # Maakt een lijst met het octale resultaat
    while quotient != 0:
        """
        Soms geeft lijn 28 de volgende error:
        TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'
        Maar waarom?
        """
        rest = quotient % 8
        quotient //= 8
        resultaat.append(rest)

    # Lijst moet omgedraaid worden
    resultaat.reverse()
    octaal = ''

    # De lijst naar een string omzetten zodat de gebruiker het kan lezen
    for i in range(len(resultaat)):
        octaal += str(resultaat[i])

    return print('Het getal %s in octaal is %s' % (decimaal, octaal))


# De hoofd functie voor het omzetten van decimaal naar octaal
def converter():
    decimaal_octaal_converter(user_input())

converter()