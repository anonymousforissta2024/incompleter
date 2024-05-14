#Source: https://stackoverflow.com/questions/57579326/lenstras-elliptic-curve-problem-with-attribute-error
from sympy import mod_inverse
import math
import secrets
from collections import namedtuple
Point = namedtuple("Point", "x y")


def point_valid(P,a,b,p):
    O = 'Inf_Point'
    if P == O:
        return True
    else:
        return (P.y**2 - (P.x**3 + a*P.x + b)) % p == 0 and 0 <= P.x < p and 0 <= P.y < p


def inverse_point(P,p):
    O = 'Inf_Point'
    # Just calculates the inverse point
    if P == O:
        return P
    return Point(P.x, (-P.y) % p)


def point_add(P, Q, a, b, p):
    O = 'Inf_Point'
    # Checking that the points are valid if not raise an exception error
    if not (point_valid(P,a,b,p) and point_valid(Q,a,b,p)):
        raise ValueError("Invalid inputs")

    if P == O:
        R = Q
    elif Q == O:
        R = P
    elif Q == inverse_point(P,p):
        R = O
    else:
        if P == Q:
            try:
                inv = mod_inverse(2 * P.y,p)
            except ValueError:
                return 2 * P.y
            dydx = (3 * P.x**2 + a) * inv
        else:
            try:
                inv =  mod_inverse(Q.x - P.x,p)
            except ValueError:
                return Q.x - P.x
            dydx = (Q.y - P.y) * inv
        x = (dydx**2 - P.x - Q.x) % p
        y = (dydx * (P.x - x) - P.y) % p
        R = Point(x, y)

    # Making sure the result is on the curve
    assert point_valid(R,a,b,p)
    # Returning the result
    return R


def point_multiply(P,n,a,b,p):
    O = 'Inf_Point'
    Q = P
    R = O
    while n > 0:
        if n % 2 == 1:
            R = point_add(R,Q,a,b,p)
        Q = point_add(Q,Q,a,b,p)
        n = math.floor(n/2)
        if n > 0:
            continue
    return R



def random_curve(N):
    while True:
        A = secrets.randbelow(N)
        x = secrets.randbelow(N)
        y = secrets.randbelow(N)
        P = Point(x,y)
        B = (y**2 - x**3 - A*x) % N

        if (4*A**3 + 27*B**2) % N != 0:
            return (A,B,P)


def lenstra(N,B):
    a,b,P = random_curve(N)
    for i in range(2,B+1):
        if type(P)== int:
            d = math.gcd(P,N)
            if d < N:
                return d
            elif d == N:
                print('start again')
        Q = point_multiply(P,i,a,b,N)
        P = Q

print(lenstra(8453621,15))