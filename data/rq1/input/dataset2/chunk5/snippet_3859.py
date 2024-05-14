#Source: https://stackoverflow.com/questions/62375315/typeerror-returnventana-missing-1-required-positional-argument-self
class Pump:    
    def __init__(self):
        print("init")

    def getPumps(self):
        pass

p = Pump.getPumps()
print(p)