#Source: https://stackoverflow.com/questions/62569070/python-typeerror-can-only-concatenate-str-not-int-to-str
import time

for i in range(2,6):
    start = time.time()
    n=i

    end = time.time()
    print(n)

    time_cost=end-start
    print(type(time_cost))
    print('totally cost for '+n+'*'+n,str(time_cost))