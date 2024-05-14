#Source: https://stackoverflow.com/questions/73316878/nameerror-name-s-is-not-defined
import scipy.stats
from numpy import sqrt, log, exp, pi

N = scipy.stats.norm.cdf
d1 = (log(S/K) + (r+sigma**2/2)*t) / (sigma*sqrt(t))
d2 = d1 - sigma * sqrt(t)

def bs_price(c_p, S, K, r, t, sigma):
    if c_p == 'c':
        return N(d1) * S - N(d2) * K * exp(-r*t)
    elif c_p == 'p':
        return N(-d2) * K * exp(-r*t) - N(-d1) * S
    else:
        return "Please specify call or put options."

MAX_TRY = 1000
def find_iv_newton(c_p, S, K, r, t, market_price):
    _sigma = 0.5
    for i in range(MAX_TRY):
        _bs_price = bs_price(c_p, S, K, r, t, sigma=_sigma)
        diff = market_price - _bs_price
        vega = S*N_prime(d1)*sqrt(t)
        if abs(diff) < ONE_CENT:
            return _sigma
        _sigma += diff/vega
    return _sigma