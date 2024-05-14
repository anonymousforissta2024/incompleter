#Source: https://stackoverflow.com/questions/61776922/python-3-exec-method-nameerror-name-of-a-defined-function-is-not-defined
def calcCycleOffset():
    global cycleOffset, uc, cs

    cycleOffset = uc - cs
    return cycleOffset


def vir_main():
    calcCycleOffset()


vir_main()
#calcCycleOffset()


print( "vir.py: cycleOffset: ", cycleOffset )