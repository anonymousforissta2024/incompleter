#Source: https://stackoverflow.com/questions/51690799/why-is-a-nameerror-raised-when-using-a-list-compression-at-the-class-level
...
class Planet:
    ATMOSPHERE_GASES = {
        'N2':(67.59, 28.0134),
        'O2':(28.04, 31.9988),
        'CO2':(0.0114, 44.00995),
        'CH4':(0.00015, 16.04303),
        'Ar':(1.105, 39.948),
        'Ne':(1.003, 20.179),
        'He':(0.719, 4.0026),
        'Kr':(0.45, 83.80),
        'H2':(0.001, 2.01594),
        'Xe':(0.23, 131.30)}
    ATMOSPHERE_GASES['Other'] = tuple([100-sum([x[0] for x in ATMOSPHERE_GASES.values()]), sum([x[1] for x in ATMOSPHERE_GASES.values()])/len(ATMOSPHERE_GASES.values())])
    ATMOSPHERE_GASES_MOLAR_MASS = sum([sum(ATMOSPHERE_GASES[x]) for x in ATMOSPHERE_GASES.keys()])/100
    ...