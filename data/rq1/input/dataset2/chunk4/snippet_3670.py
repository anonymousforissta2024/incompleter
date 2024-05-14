#Source: https://stackoverflow.com/questions/58044715/attributeerror-nonetype-object-has-no-attribute-get-balance
from upstox_api.api import *
def get_balance():
    global u, s
    return u.get_balance()