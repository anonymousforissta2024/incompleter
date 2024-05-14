#Source: https://stackoverflow.com/questions/69891656/python-typeerror-missing-1-required-positional-argument-only-when-using-threa
import sys
import multiprocessing
from multiprocessing import Process, Pool
from concurrent.futures import ThreadPoolExecutor

class GlobalValues(object):
    #singleton thread pool 
    Executor : ThreadPoolExecutor = None
    @staticmethod
    def getThreadPoolExecutor():
        if GlobalValues.Executor==None:
            GlobalValues.Executor = ThreadPoolExecutor(500)
        return GlobalValues.Executor