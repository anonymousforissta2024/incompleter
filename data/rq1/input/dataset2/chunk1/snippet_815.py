#Source: https://stackoverflow.com/questions/50736654/python-multiprocessing-typeerror
from multiprocessing import Pool
pool = Pool(processes=4)
results = pool.map(func_run, par)