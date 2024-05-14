#Source: https://stackoverflow.com/questions/72924533/attributeerror-with-extended-class-in-python
from derivations import derivation

class Derivation(derivation.Derivation):
    
    def autoderive(self, index):
        ...

deriv = derivation.Derivation()