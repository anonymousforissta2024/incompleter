#Source: https://stackoverflow.com/questions/49472108/typeerror-not-supported-between-instances-of-list-and-int
million = [1000000, "M"]
billion = [million * 1000, "B"]
trillion = [billion * 1000, "T"]
quadrillion = [trillion * 1000, "Qd"]
quintillion = [quadrillion * 1000, "Qn"]
sx = [quintillion * 1000, "Sx"]
septillion = [sx * 1000, "Sp"]

suffixes = [million, billion, trillion, quadrillion, quintillion, sx, septillion]

def getSetupResult(orevalue, furnacemultiplier, *upgrades, **kwargs):
    for i in upgrades:
        orevalue *= i
    orevalue *= furnacemultiplier
    for suffix in suffixes:
        if orevalue > suffix[0] - 1 and orevalue < suffix[0] * 1000:
            print("$"+str(orevalue)+suffix[1])

getSetupResult(quintillion,700,5,4,10,100)