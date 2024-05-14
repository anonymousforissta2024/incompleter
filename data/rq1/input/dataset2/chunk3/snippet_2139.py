#Source: https://stackoverflow.com/questions/72555433/typeerror-not-supported-between-instances-of-list-and-int-occur-whil
from multiprocessing import Pool

def f(x,y):
    return x*y

with Pool(4) as p:
    print(p.map(f,[2,2,2],[3,4,5]))