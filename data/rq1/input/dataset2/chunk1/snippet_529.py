#Source: https://stackoverflow.com/questions/63789637/python-sympy-typeerror-cant-convert-expression-to-float
from sympy.functions import sin,cos
from sympy.abc import x
from sympy import series
from pprint import pprint
# Indsæt her funktionen f(x), variablen x, udviklingspunktet x0 og antal led n
print(series(math.sqrt(x), x, x0=0, n=6))

N = int(input("Antal summer(flere summer er mere præcist): "))
a = int(input("Integrer fra: "))
b = int(input("Integrer til: "))

# Vi anvender Midpoint metoden til integration og skriver funktionen ind, som skal integreres

def integrate(N, a, b):
    def f(x):
        return series(math.sqrt(x), x, x0=0, n=6)
    value=0
    value=2
    for n in range(1, N+1):
        value += f(a+((n-(1/2))*((b-a)/N)))
    value2 = ((b-a)/N)*value
    return value2

print("...................")
print("Her er dit svar: ")
print(integrate(N, a, b))