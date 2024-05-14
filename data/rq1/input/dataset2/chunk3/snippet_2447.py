#Source: https://stackoverflow.com/questions/53148400/pathos-multiprocessing-getting-attributeerror-cant-get-attribute-someclass-o
from random import randint
import os
import pathos
mp = pathos.helpers.mp
prc = pathos.helpers.mp.Process
class SomeClass:
    def m1(self):
        self.objAttr = randint(20000,40000)
        self.selfID = id(self)
        self.m2()
    def m2(self):
        print(os.getpid(), self.objAttr,self.selfID)

    def checkMultiprocessing(self):
        for c in range(10):
            exec(f"p{c} = prc(target=self.m1)")
            exec(f"p{c}.start()")
        for c in range(10):
            exec(f"p{c}.join()")
if __name__ == "__main__":
    mp.freeze_support()
    SomeClass().checkMultiprocessing()