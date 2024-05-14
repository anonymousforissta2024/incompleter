#Source: https://stackoverflow.com/questions/51534131/name-error-name-datetime-is-not-defined
import time

"""
This is a prastise session

"""
list=[]

for i in range(10):
    list.append(datetime.datetime.now())
    time.sleep(2)