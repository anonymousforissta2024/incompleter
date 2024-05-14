#Source: https://stackoverflow.com/questions/69623498/typeerror-float-object-cannot-be-interpreted-as-an-integer
import functools

# Euclidean extended algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        d, x, y = egcd(b % a, a)
        return d, y - (b // a) * x, x

"""
    Functions whcih calculate the CRT (
    return x in ' x = a mod n'.
"""

def chinese_remainder(a, n):
    modulus = functools.reduce(lambda a, b: a * b, n)
    multipliers = []
    for N_i in n:
        N = modulus / N_i
        gcd, inverse, y = egcd(N, N_i)
        multipliers.append(inverse * N % modulus)

    result = 0
    for multi, a_i in zip(multipliers, a):
        result = (result + multi * a_i) % modulus
    return result

FN = 1184749
FM = 8118474
FL = 5386565
HN = 8686891
HM = 6036033
HK = 6029230

n = [FN, FM, FL]
a = [HN, HM, HK]

d = chinese_remainder(a, n)
number = hex(d)
print(number)