#Source: https://stackoverflow.com/questions/42547073/unhashable-type-error-whilst-finding-mode
from scipy import stats
def one_mode(l):
    return stats.mode(l)