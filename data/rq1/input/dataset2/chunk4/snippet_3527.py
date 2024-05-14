#Source: https://stackoverflow.com/questions/70837963/name-error-in-class-when-importing-my-script-file-to-another-from
from script import*

Jp = Operators(['Jp'])
Jm = Operators(['Jm'])
    
ket_1 = Single_Ket((1, 1), 1, [Jp @ Jm])

print(ket_1)