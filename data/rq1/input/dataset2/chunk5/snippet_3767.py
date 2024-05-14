#Source: https://stackoverflow.com/questions/52359991/python-3-6-nameerror-name-a-is-not-defined
def NuclearBindingEnergy(A,Z):
  a_V=15.67
  a_S=17.23
  a_C=0.75
  a_A=93.2
  a_P=0

  if A%2==1:
    a_P=0
  else:
    if Z%2==0:
      a_P=12.0
    else:
      a_P=-12.0

  B = (a_V)*A - ((a_S)*(A**(2/3))) - (a_C)*(Z**2/(A**(1/3))) - ((a_A)*(((A-(2*Z))**2)/A)) + ((a_P)/A**(1/2))

  return B

def NuclearBindingEnergyPerNucleon(A,Z):
    return NuclearBindingEnergy(A,Z)/A

print(NuclearBindingEnergy(A,Z))
print(NuclearBindingEnergy(A,Z)/A)